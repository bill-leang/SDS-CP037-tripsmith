# ✈️ Travel Itinerary Generator

A comprehensive Python-based tool that generates personalized travel itineraries using AI and real-time data from multiple APIs. The tool connects to Tavily and SerpAPI to fetch flights, hotels, and points of interest, then uses OpenAI's LLM to create detailed day-by-day itineraries, and deploys with a beautiful Streamlit web interface.

## 🌟 Features

- **Real-time Data Integration**: Fetches live data from multiple sources (Tavily, SerpAPI)
- **AI-Powered Itinerary Generation**: Uses OpenAI's GPT models to create personalized itineraries
- **Comprehensive Travel Planning**: Includes flights, hotels, activities, meals, and transportation
- **Interactive Web Interface**: Beautiful Streamlit-based UI with data visualization
- **Customizable Preferences**: Support for different travel styles, interests, and budgets
- **Export Functionality**: Export itineraries as JSON for sharing or further processing
- **Data Analysis**: Visualize travel data with interactive charts and graphs

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- API keys for:
  - OpenAI (for itinerary generation)
  - Tavily (for search functionality)
  - SerpAPI (for additional search data)

### Installation

1. **Clone or download the project files**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   ```bash
   # Copy the example environment file
   cp env_example.txt .env
   
   # Edit .env with your API keys
   nano .env
   ```

4. **Run the setup script** (optional):
   ```bash
   python setup.py
   ```

### Running the Application

#### Option 1: Streamlit Web App (Recommended)
```bash
streamlit run streamlit_app.py
```
This will open a web interface in your browser at `http://localhost:8501`

#### Option 2: Command Line Interface
```bash
python app.py
```
This provides a menu-driven interface with options to run the web app or demo.

## 📋 API Keys Setup

Create a `.env` file in the project directory with the following content:

```env
# Required API Keys
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
SERPAPI_API_KEY=your_serpapi_key_here

# Optional Settings
DEBUG=False
LOG_LEVEL=INFO
```

### Getting API Keys

1. **OpenAI API Key**:
   - Visit [OpenAI Platform](https://platform.openai.com/)
   - Create an account and generate an API key
   - Add credits to your account for API usage

2. **Tavily API Key**:
   - Visit [Tavily](https://tavily.com/)
   - Sign up for an account
   - Generate an API key from the dashboard

3. **SerpAPI Key**:
   - Visit [SerpAPI](https://serpapi.com/)
   - Create an account
   - Get your API key from the dashboard

## 🏗️ Project Structure

```
junleng-tan/
├── app.py                 # Main application entry point
├── streamlit_app.py       # Streamlit web interface
├── config.py              # Configuration management
├── models.py              # Data models and structures
├── api_clients.py         # API integration modules
├── llm_service.py         # LLM integration for itinerary generation
├── setup.py               # Setup and installation script
├── requirements.txt       # Python dependencies
├── env_example.txt        # Environment variables template
└── README.md             # This file
```

## 🔧 Usage

### Web Interface

1. **Open the Streamlit app** in your browser
2. **Fill in trip details** in the sidebar:
   - Destination city/country
   - Travel dates
   - Budget and number of travelers
   - Travel preferences (interests, style, activity level)
3. **Click "Generate Itinerary"** to create your personalized travel plan
4. **View the detailed itinerary** with daily activities, meals, and transportation
5. **Export your itinerary** as JSON or view data analysis

### Command Line Interface

Run `python app.py` and choose from:
- **Option 1**: Launch the Streamlit web app
- **Option 2**: Run a demo itinerary generation
- **Option 3**: Exit

## 📊 Features in Detail

### Data Integration
- **Flight Search**: Real-time flight options from multiple sources
- **Hotel Search**: Accommodation options with pricing and amenities
- **Points of Interest**: Tourist attractions, restaurants, and activities
- **Data Aggregation**: Combines data from multiple APIs for comprehensive results

### AI-Powered Itinerary Generation
- **Personalized Planning**: Takes into account user preferences and interests
- **Day-by-Day Structure**: Detailed daily schedules with time allocations
- **Cost Estimation**: Budget-aware planning with cost breakdowns
- **Practical Information**: Includes transportation, meal recommendations, and tips

### Web Interface Features
- **Interactive Forms**: Easy-to-use input forms for trip details
- **Real-time Generation**: Live itinerary generation with progress indicators
- **Data Visualization**: Charts and graphs for travel data analysis
- **Export Options**: Download itineraries in various formats
- **Responsive Design**: Works on desktop and mobile devices

## 🛠️ Customization

### Adding New Data Sources
To add new API integrations:

1. Create a new client class in `api_clients.py`
2. Implement the required methods for data fetching
3. Add the client to `TravelDataFetcher` class
4. Update the configuration in `config.py`

### Modifying the LLM Prompts
Edit the prompt templates in `llm_service.py` to customize:
- Itinerary structure and format
- Activity recommendations
- Cost estimation methods
- Response formatting

### UI Customization
Modify `streamlit_app.py` to:
- Change the visual design and styling
- Add new input fields
- Modify the layout and organization
- Add new visualization components

## 🐛 Troubleshooting

### Common Issues

1. **API Key Errors**:
   - Ensure all API keys are correctly set in the `.env` file
   - Verify that API keys are valid and have sufficient credits
   - Check that the `.env` file is in the correct directory

2. **Import Errors**:
   - Make sure all dependencies are installed: `pip install -r requirements.txt`
   - Check that you're using the correct Python version (3.8+)

3. **Streamlit Issues**:
   - Ensure Streamlit is installed: `pip install streamlit`
   - Try running with: `streamlit run streamlit_app.py --server.port 8501`

4. **API Rate Limits**:
   - Some APIs have rate limits; wait before retrying
   - Consider upgrading API plans for higher limits

### Debug Mode

Enable debug mode by setting `DEBUG=True` in your `.env` file for detailed error messages and logging.

## 📈 Performance Considerations

- **API Costs**: Monitor your API usage to avoid unexpected charges
- **Response Times**: Large itineraries may take longer to generate
- **Data Caching**: Consider implementing caching for frequently requested data
- **Rate Limiting**: Be mindful of API rate limits when making multiple requests

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is part of the SDS-CP037-tripsmith course work.

## 🙏 Acknowledgments

- OpenAI for providing the LLM capabilities
- Tavily and SerpAPI for data sources
- Streamlit for the web framework
- The open-source Python community

## 📞 Support

For questions or issues:
1. Check the troubleshooting section above
2. Review the code comments and documentation
3. Create an issue in the project repository

---

**Happy Traveling! ✈️🌍**