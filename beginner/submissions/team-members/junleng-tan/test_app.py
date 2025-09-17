"""
Test script for the Travel Itinerary Tool.
This script tests the core functionality without requiring API keys.
"""
import sys
import os
from datetime import date, timedelta

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that all modules can be imported."""
    print("🧪 Testing imports...")
    
    try:
        from models import TravelItinerary, DayItinerary, Flight, Hotel, PointOfInterest
        print("✅ Models imported successfully")
    except ImportError as e:
        print(f"❌ Error importing models: {e}")
        return False
    
    try:
        from config import Config
        print("✅ Config imported successfully")
    except ImportError as e:
        print(f"❌ Error importing config: {e}")
        return False
    
    return True

def test_models():
    """Test data model creation."""
    print("\n🧪 Testing data models...")
    
    try:
        from models import TravelItinerary, DayItinerary, Flight, Hotel, PointOfInterest
        
        # Test Flight model
        flight = Flight(
            airline="Test Airline",
            departure_airport="JFK",
            arrival_airport="CDG",
            departure_time="2024-06-01 14:30",
            arrival_time="2024-06-02 05:45",
            duration="7h 15m",
            price=850.0
        )
        print("✅ Flight model created successfully")
        
        # Test Hotel model
        hotel = Hotel(
            name="Test Hotel",
            address="123 Test Street",
            city="Paris",
            country="France",
            price_per_night=180.0
        )
        print("✅ Hotel model created successfully")
        
        # Test PointOfInterest model
        poi = PointOfInterest(
            name="Test Attraction",
            description="A test attraction",
            category="Landmark",
            address="456 Test Avenue",
            city="Paris",
            country="France"
        )
        print("✅ PointOfInterest model created successfully")
        
        # Test DayItinerary model
        day = DayItinerary(
            date=date(2024, 6, 1),
            city="Paris",
            activities=[{"time": "10:00", "activity": "Test Activity"}],
            meals=[{"time": "12:00", "meal": "Lunch"}]
        )
        print("✅ DayItinerary model created successfully")
        
        # Test TravelItinerary model
        itinerary = TravelItinerary(
            destination="Paris, France",
            start_date=date(2024, 6, 1),
            end_date=date(2024, 6, 5),
            duration_days=4,
            budget=2000.0,
            travelers=2,
            days=[day],
            flights=[flight],
            hotels=[hotel],
            points_of_interest=[poi]
        )
        print("✅ TravelItinerary model created successfully")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing models: {e}")
        return False

def test_config():
    """Test configuration management."""
    print("\n🧪 Testing configuration...")
    
    try:
        from config import Config
        
        # Test that config class exists and has expected attributes
        assert hasattr(Config, 'OPENAI_API_KEY')
        assert hasattr(Config, 'TAVILY_API_KEY')
        assert hasattr(Config, 'SERPAPI_API_KEY')
        assert hasattr(Config, 'DEBUG')
        assert hasattr(Config, 'LOG_LEVEL')
        
        print("✅ Config class structure is correct")
        
        # Test validation method exists
        assert hasattr(Config, 'validate_required_keys')
        assert hasattr(Config, 'get_api_key')
        
        print("✅ Config methods are available")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing config: {e}")
        return False

def test_demo_functionality():
    """Test the demo functionality."""
    print("\n🧪 Testing demo functionality...")
    
    try:
        from demo import create_sample_itinerary, display_itinerary_summary
        
        # Create sample itinerary
        itinerary = create_sample_itinerary()
        assert itinerary is not None
        assert len(itinerary.days) > 0
        assert len(itinerary.flights) > 0
        assert len(itinerary.hotels) > 0
        assert len(itinerary.points_of_interest) > 0
        
        print("✅ Demo itinerary creation works")
        
        # Test display function (should not raise exception)
        display_itinerary_summary(itinerary)
        print("✅ Demo display function works")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing demo functionality: {e}")
        return False

def main():
    """Main test function."""
    print("🧪 Travel Itinerary Tool - Test Suite")
    print("=" * 50)
    
    tests = [
        ("Import Test", test_imports),
        ("Model Test", test_models),
        ("Config Test", test_config),
        ("Demo Test", test_demo_functionality)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 Running {test_name}...")
        if test_func():
            passed += 1
            print(f"✅ {test_name} PASSED")
        else:
            print(f"❌ {test_name} FAILED")
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The application is ready to use.")
        print("\nNext steps:")
        print("1. Set up your API keys in the .env file")
        print("2. Run: python app.py")
        print("3. Or run: streamlit run streamlit_app.py")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
