# 🌍 AI-Based-Travel-Agent

An intelligent travel planning application powered by **LangChain**, **LangGraph**, and **OpenAI** that helps users plan complete trips with real-time cost calculations, weather information, and detailed itineraries.

![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-FF4B4B?style=flat-square&logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?style=flat-square&logo=openai)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Architecture](#architecture)
- [API Keys](#api-keys)
- [Tools & Capabilities](#tools--capabilities)
- [Example Queries](#example-queries)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The **AI Travel Agent** is a sophisticated travel planning assistant that combines:
- 🤖 **AI Intelligence** using OpenAI's GPT-4o-mini model
- 🔄 **Agent Orchestration** via LangGraph for multi-step reasoning
- 🛠️ **Tool Integration** for real-time data fetching
- 💰 **Cost Calculations** with arithmetic operations
- 🌤️ **Weather Integration** for destination planning
- 📍 **Search Capabilities** via Google Serper API with DuckDuckGo fallback

The agent follows a structured 5-step process to generate comprehensive travel plans with budget breakdowns, daily itineraries, and multimedia resources.

---

## Features

### Core Capabilities

✨ **Comprehensive Trip Planning**
- Multi-day itinerary generation
- Budget allocation and cost breakdown
- Daily activity recommendations

🌤️ **Weather Information**
- Real-time weather data for destinations
- Climate considerations for packing/activities
- Temperature and condition forecasts

🏨 **Accommodation Search**
- Hotel discovery with pricing
- Price filtering based on budget
- Location and amenity details

🏛️ **Attractions & Activities**
- Top tourist attractions discovery
- Entry fees and pricing information
- Activity duration and recommendations

🍽️ **Dining Options**
- Restaurant recommendations
- Price range and cuisine details
- Popular dishes and reviews

💰 **Cost Management**
- Real-time price calculations
- Currency conversion for international trips
- Budget optimization suggestions
- Daily expense breakdown

🎥 **Multimedia Resources**
- YouTube video recommendations
- Travel guides and vlogs
- Destination inspiration content

🔄 **Intelligent Search**
- Primary: Google Serper API integration
- Fallback: DuckDuckGo search
- Automatic fallback if primary unavailable

---

## Prerequisites

### System Requirements
- **Python**: 3.8 or higher
- **OS**: Windows, macOS, or Linux
- **RAM**: 4GB minimum (8GB recommended)

### Required API Keys
You'll need to obtain the following API keys:

1. **[OpenAI API](https://platform.openai.com/api-keys)** - Core AI engine
   - Sign up at OpenAI website
   - Create new API key
   - Keep it secret and secure

2. **[Google Serper API](https://serper.dev)** - Web search
   - Create free account (100 free searches/month)
   - Generate API key
   - _Optional: DuckDuckGo used as fallback if unavailable_

3. **[OpenWeatherMap API](https://openweathermap.org/api)** - Weather data
   - Sign up for free tier
   - Generate API key
   - _Optional: Weather feature disabled if unavailable_

---

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/kshitijkasabekar/AI-Based-Travel-Agent.git
cd AI-Based-Travel-Agent
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Create `.env` File
Create a `.env` file in the project root directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
SERPER_API_KEY=your_serper_api_key_here
OPENWEATHERMAP_API_KEY=your_openweathermap_api_key_here
```

⚠️ **Security Note**: Never commit `.env` file to version control. It's already in `.gitignore`.

---

## Configuration

### Environment Variables

| Variable | Required | Description | Default |
|----------|----------|-------------|---------|
| `OPENAI_API_KEY` | ✅ Yes | OpenAI API key for GPT-4o-mini model | None |
| `SERPER_API_KEY` | ⚠️ Optional | Google Serper API key for web search | DuckDuckGo fallback |
| `OPENWEATHERMAP_API_KEY` | ⚠️ Optional | OpenWeatherMap API key for weather | Weather disabled |

### Model Configuration
- **Model**: `gpt-4o-mini` (cost-effective, fast)
- **Temperature**: `0` (deterministic responses)
- **Max Tokens**: `2000` (comprehensive outputs)

---

## Usage

### Running the Application
```bash
streamlit run app.py
```

The application will open at `http://localhost:8501` in your default browser.

### Step-by-Step Guide

1. **Check API Status** - View sidebar for API key status
2. **Select Query Type** - Choose from examples or enter custom query
3. **Enter Travel Details** - Specify destination, budget, preferences
4. **Click "Plan My Trip"** - Agent processes and generates plan
5. **Review Results** - View itinerary, costs, and resources

### Basic Query Template
```
I want to visit [destination] for [number] days.
Budget: [amount] [currency].
Preferences: [activities, dining, accommodation style].
Special requirements: [any specific needs].
```

---

## Project Structure

```
AI-Based-Travel-Agent/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── .env                            # Environment variables (create this)
├── .gitignore                      # Git ignore configuration
├── README.md                       # Documentation (this file)
└── LICENSE                         # MIT License
```

### File Descriptions

| File | Purpose |
|------|---------|
| `app.py` | Main application with Streamlit UI and agent logic |
| `requirements.txt` | All Python package dependencies |
| `.env` | API keys and configuration (not committed) |
| `.gitignore` | Git rules to exclude sensitive files |

---

## Architecture

### Agent Flow Diagram
```
User Query
    ↓
LLM Decision Node
    ↓
Tool Execution (get_weather, search, calculations)
    ↓
LLM Processing
    ↓
Return Results
    ↓
Format & Display
```

### Key Components

#### 1. **LangChain Integration**
- LLM binding with tools
- Tool execution management
- Message history handling

#### 2. **LangGraph State Machine**
- Multi-step agent reasoning
- Tool node for parallel execution
- Conditional routing based on tool calls

#### 3. **Tools Available**

| Tool | Purpose | Input |
|------|---------|-------|
| `get_weather()` | Fetch weather data | City name |
| `search_google()` | Web search via Serper | Query string |
| `search_duck()` | Web search via DuckDuckGo | Query string |
| `youtube_search()` | Find YouTube videos | Query string |
| `addition()` | Add two numbers | Two integers |
| `multiply()` | Multiply two numbers | Two integers |
| `division()` | Divide two numbers | Two integers |
| `substraction()` | Subtract two numbers | Two integers |
| `python_repl` | Execute Python code | Python code |

---

## API Keys

### Getting OpenAI API Key
1. Go to https://platform.openai.com/api-keys
2. Click "Create new secret key"
3. Copy and paste in `.env`

### Getting Serper API Key
1. Visit https://serper.dev
2. Sign up for free account
3. Go to API section and copy key
4. Paste in `.env`

### Getting OpenWeatherMap API Key
1. Visit https://openweathermap.org/api
2. Sign up for free
3. Go to API keys section
4. Copy and paste in `.env`

---

## Tools & Capabilities

### Weather Tool (`get_weather`)
```python
# Fetches real-time weather information
weather_data = get_weather("Paris")
# Returns: Temperature, conditions, humidity, etc.
```

### Search Tools (`search_google`, `search_duck`)
```python
# Primary search (Google Serper)
results = search_google("best hotels in Tokyo budget under $50")

# Fallback search (DuckDuckGo)
results = search_duck("restaurants in Barcelona")
```

### Arithmetic Tools
```python
# Cost calculations
total = addition(5000, 3000)           # 8000
daily_cost = division(30000, 5)        # 6000 per day
transport = multiply(500, 4)           # 2000 for 4 trips
```

### YouTube Tool
```python
# Find travel videos
videos = youtube_search("Goa beaches travel vlog 2024")
```

---

## Example Queries

### Example 1: Beach Vacation to Goa
```
I want to visit Goa for 5 days in December.
My budget is 30,000 INR.
Get current weather for Goa.
Find hotels under 3,000 INR per night.
Activities: Water sports, beaches, nightlife.
Food budget: 500 INR/day.
Also show YouTube videos.
```

**Expected Output:**
- Current weather and conditions
- Hotel recommendations with prices
- Daily itinerary with activities
- Cost breakdown (accommodation, food, activities)
- YouTube travel videos

### Example 2: International Trip to Thailand
```
I want to visit Thailand for 4 days.
Budget: 800 USD.
Convert costs to INR.
Get Bangkok weather.
Find hotels under 30 USD per night.
Include: Temples, street food, transport, shopping.
Show YouTube videos for travel inspiration.
```

**Expected Output:**
- Currency conversion (USD to INR)
- Bangkok weather conditions
- Budget-friendly hotel options
- Daily temple and market itinerary
- Food recommendations with pricing
- Total cost breakdown with conversions

---

## System Prompt Strategy

The AI agent is guided by a comprehensive system prompt that ensures:

1. **Weather First**: Always fetch current weather conditions
2. **Comprehensive Search**: Search for hotels, attractions, restaurants, transportation
3. **Cost Accuracy**: Use arithmetic tools for all calculations
4. **Currency Support**: Search and convert currency when needed
5. **Multimedia**: Include YouTube videos for inspiration
6. **Structured Format**: Present output in consistent sections

---

## Output Format

The agent generates responses in a structured format:

```markdown
## 🌤️ Weather Information
[Current weather, temperature, conditions]

## 💱 Currency Conversion  
[Exchange rates if international]

## 🏛️ Attractions & Activities
[Top attractions with entry fees]

## 🏨 Hotels & Accommodation
[Hotel options with pricing]

## 📅 Daily Itinerary
[Day-by-day schedule with times]

## 💰 Cost Breakdown
[Itemized expenses and totals]

## 🎥 YouTube Resources
[Relevant video recommendations]

## 📋 Summary
[Key highlights and recommendations]
```

---

## Error Handling

The application includes robust error handling:

### API Key Validation
- ✅ Shows status in sidebar
- ⚠️ Graceful degradation if optional keys missing
- ❌ Stops execution if critical keys missing

### Search Fallback
- 🔄 Primary: Google Serper API
- 🔄 Fallback: DuckDuckGo (automatic)
- 📝 Error messages for complete failures

### Session Management
- 📝 Chat history preservation
- 🔄 Agent reinitialization if needed
- 💾 State management across interactions

---

## Troubleshooting

### Common Issues

**❌ "OPENAI_API_KEY missing from .env file"**
- **Solution**: Create `.env` file in root directory with OpenAI API key
- Verify file is in correct location
- Restart the application

**❌ "Google search unavailable"**
- **Solution**: Check SERPER_API_KEY in `.env`
- DuckDuckGo fallback will activate automatically
- Application continues with reduced functionality

**⚠️ "Weather data unavailable"**
- **Solution**: Add OPENWEATHERMAP_API_KEY to `.env`
- Check if city name is spelled correctly
- Weather module is optional; agent continues without it

**❌ "Slow responses"**
- **Solution**: Check internet connection
- OpenAI API might be rate-limited
- Wait before making next request
- Check OpenAI service status

**❌ "Module not found errors"**
- **Solution**: Reinstall requirements
  ```bash
  pip install -r requirements.txt --force-reinstall
  ```
- Ensure virtual environment is activated
- Check Python version (3.8+)

---

## Dependencies

### Core Framework
- **streamlit** (>=1.28.0) - Web UI framework
- **langchain** (>=0.1.0) - LLM framework
- **langchain-openai** (>=0.1.0) - OpenAI integration
- **langgraph** (>=0.0.45) - Agent orchestration

### AI & Language
- **openai** (>=1.0.0) - OpenAI API client
- **langchain-core** (>=0.1.0) - Core components
- **langchain-community** (>=0.0.29) - Community integrations
- **langchain-experimental** (>=0.0.56) - Experimental features

### Search & Data
- **google-search-results** (>=2.4.2) - Google Serper API
- **duckduckgo-search** (>=4.0.0) - DuckDuckGo search
- **youtube-search-python** (>=1.6.6) - YouTube search
- **pyowm** (>=3.3.0) - Weather API wrapper

### Utilities
- **python-dotenv** (>=1.0.0) - Environment variable management
- **pandas** (>=2.0.0) - Data manipulation
- **numpy** (>=1.24.0) - Numerical computing
- **requests** (>=2.31.0) - HTTP requests
- **httpx** (>=0.24.0) - HTTP client
- **pydantic** (>=2.0.0) - Data validation
- **Pillow** (>=10.0.0) - Image processing

---

## Performance Optimization

### Tips for Better Performance

1. **Concurrent API Calls**: Agent uses parallel tool execution
2. **Caching**: Streamlit caches computations automatically
3. **Temperature = 0**: Ensures consistent, faster responses
4. **Token Limit**: 2000 tokens prevent excessively long outputs

### Typical Execution Time
- Initial request: 15-30 seconds
- Subsequent requests: 10-20 seconds
- Depends on API response times

---

## Security Considerations

✅ **Best Practices**

1. **Never commit `.env`** - Already in `.gitignore`
2. **Use environment variables** - Don't hardcode API keys
3. **Rotate API keys** - Periodically refresh keys
4. **Rate limiting** - Implement if deploying publicly
5. **Input validation** - Agent validates user queries
6. **HTTPS only** - Use secure connections when deployed

---

## Future Enhancements

🚀 **Planned Features**

- [ ] Flight price integration
- [ ] Real-time train/bus booking
- [ ] User authentication and saved trips
- [ ] Multi-language support
- [ ] Mobile app version
- [ ] Integration with booking platforms (Booking.com, Expedia)
- [ ] Expense tracking during trip
- [ ] Real-time translation
- [ ] Travel insurance recommendations
- [ ] Visa requirement checker

---

## Contributing

Contributions are welcome! Here's how:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Guidelines
- Follow PEP 8 style guide
- Add comments for complex logic
- Test thoroughly before submitting
- Update README if adding features

---

## License

This project is open source and available under the **MIT License** - see the LICENSE file for details.

---

## Support & Contact

For issues, questions, or suggestions:

- 🐛 **Report bugs**: Open an issue on GitHub
- 💡 **Feature requests**: Create a GitHub discussion
- 📧 **Contact**: [Your Contact Info]
- 📚 **Documentation**: Check the README and code comments

---

## Acknowledgments

- **OpenAI** - GPT-4o-mini language model
- **LangChain** - LLM framework and tools
- **LangGraph** - Agent orchestration
- **Streamlit** - Web application framework
- **Google Serper** - Web search API
- **OpenWeatherMap** - Weather data API

---

## Changelog

### Version 1.0.0 (Initial Release)
- ✨ Core AI travel agent functionality
- 🌤️ Weather integration
- 🔍 Multi-source search capabilities
- 💰 Cost calculation engine
- 📅 Itinerary generation
- 🎥 YouTube video recommendations

---

## Disclaimer

This project is for educational and personal use. Travel recommendations are AI-generated and should be verified with official sources before booking. The developers are not responsible for any inaccuracies in API data or recommendations.

---

<div align="center">

**Built with ❤️ using Streamlit, LangChain, and OpenAI**

[⭐ Star this repo](#) • [🐛 Report Issue](#) • [📝 Contribute](#)

</div>