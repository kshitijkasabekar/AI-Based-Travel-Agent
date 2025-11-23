import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.tools import tool
from langchain_community.utilities import OpenWeatherMapAPIWrapper, GoogleSerperAPIWrapper
from langchain_community.tools import DuckDuckGoSearchRun, YouTubeSearchTool
from langchain_core.tools import Tool
from langchain_experimental.utilities import PythonREPL
from langgraph.graph import MessagesState, StateGraph, END, START
from langgraph.prebuilt import ToolNode, tools_condition

# Page configuration
st.set_page_config(
    page_title="🌍 AI Travel Agent",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load environment variables from .env
load_dotenv()

# Initialize session state
if 'travel_agent' not in st.session_state:
    st.session_state.travel_agent = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Custom Tools
@tool
def addition(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b

@tool
def division(a: int, b: int) -> float:
    """Divide two integers."""
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b

@tool
def substraction(a: int, b: int) -> float:
    """Subtract two integers."""
    return a - b

@tool
def get_weather(city: str) -> str:
    """Fetches the current weather of the city from OpenWeatherMap."""
    try:
        weather_api_key = os.getenv("OPENWEATHERMAP_API_KEY")
        if weather_api_key:
            os.environ["OPENWEATHERMAP_API_KEY"] = weather_api_key
            weather = OpenWeatherMapAPIWrapper()
            return weather.run(city)
        else:
            return f"⚠️ Missing OPENWEATHERMAP_API_KEY in .env."
    except Exception as e:
        return f"Weather data unavailable for {city}. Error: {str(e)}"

@tool
def search_google(query: str) -> str:
    """Fetches details about attractions, restaurants, hotels, etc. from Google Serper API."""
    try:
        serper_api_key = os.getenv("SERPER_API_KEY")
        if serper_api_key:
            os.environ["SERPER_API_KEY"] = serper_api_key
            search_serper = GoogleSerperAPIWrapper()
            return search_serper.run(query)
        else:
            return search_duck(query)  # fallback
    except Exception as e:
        return f"Google search unavailable. Error: {str(e)}"

@tool
def search_duck(query: str) -> str:
    """Fetches details using DuckDuckGo search."""
    try:
        search_d = DuckDuckGoSearchRun()
        return search_d.invoke(query)
    except Exception as e:
        return f"DuckDuckGo search unavailable. Error: {str(e)}"

@tool
def youtube_search(query: str) -> str:
    """Fetches YouTube videos about travel destinations."""
    try:
        youtubetool = YouTubeSearchTool()
        return youtubetool.run(query)
    except Exception as e:
        return f"YouTube search unavailable. Error: {str(e)}"

# Python REPL tool
python_repl = PythonREPL()
repl_tool = Tool(
    name="python_repl",
    description="A Python shell for complex calculations. Input should be a valid python command.",
    func=python_repl.run,
)

def initialize_travel_agent():
    """Initialize the travel agent with all tools and configurations."""
    try:
        openai_api_key = os.getenv("OPENAI_API_KEY")
        
        if not openai_api_key:
            st.error("❌ OPENAI_API_KEY missing from .env file.")
            return None
        
        llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0,
            max_tokens=2000,
            api_key=openai_api_key
        )
        
        system_prompt = SystemMessage("""
        You are a professional AI Travel Agent. You MUST follow this EXACT process for every travel query:

        STEP 1: ALWAYS call get_weather tool first for the destination city

        STEP 2: ALWAYS call search_google or search_duck to find:
           - Hotels with specific prices per night
           - Top attractions with entry fees
           - Restaurants with price ranges
           - Transportation options with costs
           - CURRENCY CONVERSION: Search for exchange rate

        STEP 3: Use arithmetic tools (addition, multiply, division) to perform ALL cost calculations

        STEP 4: Call youtube_search for relevant videos

        STEP 5: Provide a detailed itinerary with real costs from tool results

        FORMAT:
        ## 🌤️ Weather Information
        ## 💱 Currency Conversion  
        ## 🏛️ Attractions & Activities
        ## 🏨 Hotels & Accommodation
        ## 📅 Daily Itinerary
        ## 💰 Cost Breakdown
        ## 🎥 YouTube Resources
        ## 📋 Summary
        """)
        
        tools = [
            addition, multiply, division, substraction,
            get_weather, search_google, search_duck,
            repl_tool, youtube_search
        ]
        
        llm_with_tools = llm.bind_tools(tools)
        
        def function_1(state: MessagesState):
            user_question = state["messages"]
            input_question = [system_prompt] + user_question
            response = llm_with_tools.invoke(input_question)
            return {"messages": [response]}
        
        builder = StateGraph(MessagesState)
        builder.add_node("llm_decision_step", function_1)
        builder.add_node("tools", ToolNode(tools))
        builder.add_edge(START, "llm_decision_step")
        builder.add_conditional_edges("llm_decision_step", tools_condition)
        builder.add_edge("tools", "llm_decision_step")
        
        react_graph = builder.compile()
        return react_graph
        
    except Exception as e:
        st.error(f"❌ Error initializing travel agent: {str(e)}")
        return None

def main():
    # Header
    st.markdown("""
    <div style='text-align: center; padding: 2rem 0; 
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); 
    color: white; border-radius: 10px; margin-bottom: 2rem;'>
        <h1>🌍 AI Travel Agent & Expense Planner</h1>
        <p>Plan your perfect trip with real-time data and detailed cost calculations</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar API Status
    st.sidebar.header("📡 API Status")
    
    openai_key = os.getenv("OPENAI_API_KEY")
    serper_key = os.getenv("SERPER_API_KEY")
    weather_key = os.getenv("OPENWEATHERMAP_API_KEY")
    
    st.sidebar.success("✅ OPENAI_API_KEY Loaded") if openai_key else st.sidebar.error("❌ Missing OPENAI_API_KEY")
    st.sidebar.success("✅ SERPER_API_KEY Loaded") if serper_key else st.sidebar.warning("⚠️ SERPER_API_KEY Missing (DuckDuckGo fallback)")
    st.sidebar.success("✅ OPENWEATHERMAP_API_KEY Loaded") if weather_key else st.sidebar.warning("⚠️ OPENWEATHERMAP_API_KEY Missing (Weather disabled)")

    st.header("💬 Travel Query")
    
    # Example queries
    example_queries = {
        "🏖️ Beach Vacation": """I want to visit Goa for 5 days in December.
My budget is 30,000 INR.
Get current weather for Goa.
Find hotels under 3,000 INR per night.
Water sports, beaches, nightlife.
Food budget: 500 INR/day.
Also show YouTube videos.""",
        
        "🌍 International Trip": """I want to visit Thailand for 4 days.
Budget: 800 USD.
Convert costs to INR.
Get Bangkok weather.
Hotels under 30 USD.
Include food, temples, transport.
Show YouTube videos."""
    }
    
    selected_example = st.selectbox(
        "🎯 Choose Example Query:", 
        ["Custom Query"] + list(example_queries.keys())
    )
    
    query = st.text_area(
        "✍️ Your Travel Query:",
        value=example_queries[selected_example] if selected_example != "Custom Query" else "",
        height=200
    )
    
    # Process button
    if st.button("🚀 Plan My Trip", type="primary", use_container_width=True):
        if not query.strip():
            st.warning("Please enter your travel query!")
            return
        
        if not openai_key:
            st.error("❌ OPENAI_API_KEY missing from .env")
            return
        
        if st.session_state.travel_agent is None:
            with st.spinner("🔧 Initializing AI Travel Agent..."):
                st.session_state.travel_agent = initialize_travel_agent()
        
        if st.session_state.travel_agent is None:
            st.error("❌ Initialization failed. Check your .env keys.")
            return
        
        with st.spinner("🤖 Planning your perfect trip..."):
            try:
                response = st.session_state.travel_agent.invoke({
                    "messages": [HumanMessage(query)]
                })
                
                if response and "messages" in response:
                    final_response = response["messages"][-1].content
                    st.success("✅ Your travel plan is ready!")
                    st.markdown(final_response)
                    
                    st.session_state.chat_history.append({
                        "query": query,
                        "response": final_response
                    })
                else:
                    st.error("❌ No response received.")
                    
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
