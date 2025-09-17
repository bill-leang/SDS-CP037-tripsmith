"""
Travel Itinerary Tool - Main Application
A comprehensive tool for generating personalized travel itineraries using AI and real-time data.
"""
import sys
import os
from config import Config
from api_clients import TravelDataFetcher
from llm_service import ItineraryGenerator

def test_api_connections():
    """Test API connections and display status."""
    print("🔍 Testing API Connections...")
    print("=" * 40)
    
    # Test configuration
    try:
        Config.validate_required_keys()
        print("✅ Configuration loaded successfully!")
        print(f"Debug mode: {Config.DEBUG}")
        print(f"Log level: {Config.LOG_LEVEL}")
    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
        print("\nTo fix this:")
        print("1. Copy env_example.txt to .env")
        print("2. Fill in your actual API keys in the .env file")
        print("3. Make sure .env is in your .gitignore")
        return False
    
    # Test API clients
    print("\n🧪 Testing API Clients...")
    
    try:
        data_fetcher = TravelDataFetcher()
        print("✅ TravelDataFetcher initialized successfully!")
    except Exception as e:
        print(f"❌ Error initializing TravelDataFetcher: {e}")
    
    try:
        itinerary_generator = ItineraryGenerator()
        print("✅ ItineraryGenerator initialized successfully!")
    except Exception as e:
        print(f"❌ Error initializing ItineraryGenerator: {e}")
    
    return True

def demo_itinerary_generation():
    """Demonstrate itinerary generation with sample data."""
    print("\n🎯 Demo: Generating Sample Itinerary...")
    print("=" * 40)
    
    try:
        # Sample data
        destination = "Paris, France"
        start_date = "2024-06-01"
        end_date = "2024-06-05"
        budget = 2000
        travelers = 2
        
        preferences = {
            'interests': ['Culture', 'Food', 'History'],
            'travel_style': 'Mid-range',
            'activity_level': 'Moderate',
            'food_preferences': ['Local Cuisine', 'Fine Dining']
        }
        
        print(f"Destination: {destination}")
        print(f"Dates: {start_date} to {end_date}")
        print(f"Budget: ${budget}")
        print(f"Travelers: {travelers}")
        
        # Fetch travel data
        print("\n📡 Fetching travel data...")
        data_fetcher = TravelDataFetcher()
        travel_data = data_fetcher.get_comprehensive_data(
            destination=destination,
            start_date=start_date,
            end_date=end_date,
            origin="New York, USA",
            budget=budget
        )
        
        print(f"✅ Found {len(travel_data.get('flights', []))} flight options")
        print(f"✅ Found {len(travel_data.get('hotels', []))} hotel options")
        print(f"✅ Found {len(travel_data.get('pois', []))} points of interest")
        
        # Generate itinerary
        print("\n🤖 Generating itinerary with AI...")
        itinerary_generator = ItineraryGenerator()
        itinerary = itinerary_generator.generate_itinerary(
            destination=destination,
            start_date=start_date,
            end_date=end_date,
            budget=budget,
            travelers=travelers,
            preferences=preferences,
            travel_data=travel_data
        )
        
        print("✅ Itinerary generated successfully!")
        print(f"📅 {len(itinerary.days)} days planned")
        
        # Display summary
        summary = itinerary_generator.generate_summary(itinerary)
        print("\n" + summary)
        
    except Exception as e:
        print(f"❌ Error in demo: {e}")

def main():
    """Main application function."""
    print("✈️ Travel Itinerary Tool")
    print("=" * 50)
    
    # Test API connections
    if not test_api_connections():
        return
    
    # Ask user what they want to do
    print("\nWhat would you like to do?")
    print("1. Run the Streamlit web app")
    print("2. Run a demo itinerary generation")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        print("\n🚀 Starting Streamlit app...")
        print("The app will open in your browser.")
        print("Press Ctrl+C to stop the server.")
        os.system("streamlit run streamlit_app.py")
    elif choice == "2":
        demo_itinerary_generation()
    elif choice == "3":
        print("👋 Goodbye!")
    else:
        print("❌ Invalid choice. Please run the script again.")

if __name__ == "__main__":
    main()
