"""
Demo script for the Travel Itinerary Tool.
This script demonstrates the core functionality without requiring API keys.
"""
import json
from datetime import datetime, date, timedelta
from models import TravelItinerary, DayItinerary, Flight, Hotel, PointOfInterest

def create_sample_data():
    """Create sample travel data for demonstration."""
    
    # Sample flights
    flights = [
        Flight(
            airline="Air France",
            departure_airport="JFK",
            arrival_airport="CDG",
            departure_time="2024-06-01 14:30",
            arrival_time="2024-06-02 05:45",
            duration="7h 15m",
            price=850.0,
            flight_number="AF123"
        ),
        Flight(
            airline="Delta",
            departure_airport="JFK",
            arrival_airport="CDG",
            departure_time="2024-06-01 18:45",
            arrival_time="2024-06-02 10:00",
            duration="7h 15m",
            price=920.0,
            flight_number="DL456"
        )
    ]
    
    # Sample hotels
    hotels = [
        Hotel(
            name="Hotel des Invalides",
            address="129 Rue de Grenelle, 75007 Paris",
            city="Paris",
            country="France",
            price_per_night=180.0,
            rating=4.5,
            amenities=["WiFi", "Breakfast", "Gym", "Spa"],
            check_in="2024-06-02",
            check_out="2024-06-06"
        ),
        Hotel(
            name="Le Meurice",
            address="228 Rue de Rivoli, 75001 Paris",
            city="Paris",
            country="France",
            price_per_night=450.0,
            rating=4.8,
            amenities=["WiFi", "Breakfast", "Concierge", "Spa", "Restaurant"],
            check_in="2024-06-02",
            check_out="2024-06-06"
        )
    ]
    
    # Sample points of interest
    pois = [
        PointOfInterest(
            name="Eiffel Tower",
            description="Iconic iron lattice tower and symbol of Paris",
            category="Landmark",
            address="Champ de Mars, 7th arrondissement",
            city="Paris",
            country="France",
            rating=4.6,
            price_range="€15-25",
            opening_hours="9:30 AM - 11:45 PM"
        ),
        PointOfInterest(
            name="Louvre Museum",
            description="World's largest art museum and historic monument",
            category="Museum",
            address="Rue de Rivoli, 75001 Paris",
            city="Paris",
            country="France",
            rating=4.5,
            price_range="€17",
            opening_hours="9:00 AM - 6:00 PM"
        ),
        PointOfInterest(
            name="Notre-Dame Cathedral",
            description="Medieval Catholic cathedral",
            category="Religious Site",
            address="6 Parvis Notre-Dame - Pl. Jean-Paul II, 75004 Paris",
            city="Paris",
            country="France",
            rating=4.4,
            price_range="Free",
            opening_hours="8:00 AM - 6:45 PM"
        )
    ]
    
    return {
        'flights': flights,
        'hotels': hotels,
        'pois': pois
    }

def create_sample_itinerary():
    """Create a sample travel itinerary."""
    
    start_date = date(2024, 6, 2)
    end_date = date(2024, 6, 6)
    
    # Day 1
    day1 = DayItinerary(
        date=start_date,
        city="Paris",
        activities=[
            {
                "time": "10:00",
                "activity": "Eiffel Tower Visit",
                "description": "Visit the iconic Eiffel Tower and enjoy panoramic views of Paris",
                "duration": "2 hours",
                "cost": 25.0,
                "location": "Champ de Mars, 7th arrondissement"
            },
            {
                "time": "14:00",
                "activity": "Seine River Cruise",
                "description": "Relaxing boat cruise along the Seine River",
                "duration": "1 hour",
                "cost": 15.0,
                "location": "Seine River"
            }
        ],
        meals=[
            {
                "time": "12:30",
                "meal": "Lunch",
                "restaurant": "Café de Flore",
                "description": "Traditional French bistro experience",
                "cost": 45.0,
                "location": "172 Boulevard Saint-Germain"
            },
            {
                "time": "19:30",
                "meal": "Dinner",
                "restaurant": "Le Comptoir du Relais",
                "description": "Cozy bistro with excellent French cuisine",
                "cost": 65.0,
                "location": "9 Carrefour de l'Odéon"
            }
        ],
        transportation=[
            {
                "from": "Hotel",
                "to": "Eiffel Tower",
                "method": "Metro Line 6",
                "cost": 2.10,
                "duration": "15 minutes"
            }
        ]
    )
    
    # Day 2
    day2 = DayItinerary(
        date=start_date + timedelta(days=1),
        city="Paris",
        activities=[
            {
                "time": "09:00",
                "activity": "Louvre Museum",
                "description": "Explore the world's largest art museum",
                "duration": "4 hours",
                "cost": 17.0,
                "location": "Rue de Rivoli, 75001"
            },
            {
                "time": "15:00",
                "activity": "Tuileries Garden Walk",
                "description": "Stroll through the beautiful Tuileries Garden",
                "duration": "1 hour",
                "cost": 0.0,
                "location": "Place de la Concorde"
            }
        ],
        meals=[
            {
                "time": "13:00",
                "meal": "Lunch",
                "restaurant": "Café Marly",
                "description": "Elegant café with Louvre views",
                "cost": 35.0,
                "location": "93 Rue de Rivoli"
            }
        ],
        transportation=[
            {
                "from": "Hotel",
                "to": "Louvre",
                "method": "Walking",
                "cost": 0.0,
                "duration": "20 minutes"
            }
        ]
    )
    
    # Create main itinerary
    itinerary = TravelItinerary(
        destination="Paris, France",
        start_date=start_date,
        end_date=end_date,
        duration_days=4,
        budget=2000.0,
        travelers=2,
        days=[day1, day2],
        flights=create_sample_data()['flights'],
        hotels=create_sample_data()['hotels'],
        points_of_interest=create_sample_data()['pois']
    )
    
    return itinerary

def display_itinerary_summary(itinerary):
    """Display a summary of the itinerary."""
    print("✈️ Travel Itinerary Summary")
    print("=" * 50)
    print(f"Destination: {itinerary.destination}")
    print(f"Duration: {itinerary.duration_days} days")
    print(f"Travelers: {itinerary.travelers}")
    print(f"Budget: ${itinerary.budget:,.2f}")
    print(f"Dates: {itinerary.start_date} to {itinerary.end_date}")
    
    print(f"\n📅 Daily Itinerary:")
    for i, day in enumerate(itinerary.days, 1):
        print(f"\nDay {i} - {day.date.strftime('%A, %B %d, %Y')}")
        print(f"📍 {day.city}")
        
        if day.activities:
            print("  🎯 Activities:")
            for activity in day.activities:
                print(f"    • {activity['time']} - {activity['activity']}")
                print(f"      {activity['description']}")
                print(f"      💰 ${activity['cost']:.2f} | ⏱️ {activity['duration']}")
        
        if day.meals:
            print("  🍽️ Meals:")
            for meal in day.meals:
                print(f"    • {meal['time']} - {meal['meal']} at {meal['restaurant']}")
                print(f"      {meal['description']}")
                print(f"      💰 ${meal['cost']:.2f}")
    
    print(f"\n✈️ Flight Options:")
    for flight in itinerary.flights:
        print(f"  • {flight.airline} {flight.flight_number}")
        print(f"    {flight.departure_airport} → {flight.arrival_airport}")
        print(f"    {flight.departure_time} - {flight.arrival_time}")
        print(f"    💰 ${flight.price:.2f}")
    
    print(f"\n🏨 Hotel Options:")
    for hotel in itinerary.hotels:
        print(f"  • {hotel.name}")
        print(f"    {hotel.address}")
        print(f"    💰 ${hotel.price_per_night:.2f}/night | ⭐ {hotel.rating}")
    
    print(f"\n🎯 Points of Interest:")
    for poi in itinerary.points_of_interest:
        print(f"  • {poi.name}")
        print(f"    {poi.description}")
        print(f"    💰 {poi.price_range} | ⭐ {poi.rating}")

def export_itinerary_json(itinerary, filename="sample_itinerary.json"):
    """Export itinerary to JSON file."""
    itinerary_dict = {
        'destination': itinerary.destination,
        'start_date': itinerary.start_date.isoformat(),
        'end_date': itinerary.end_date.isoformat(),
        'budget': itinerary.budget,
        'travelers': itinerary.travelers,
        'days': [
            {
                'date': day.date.isoformat(),
                'city': day.city,
                'activities': day.activities,
                'meals': day.meals,
                'transportation': day.transportation
            }
            for day in itinerary.days
        ],
        'flights': [
            {
                'airline': flight.airline,
                'departure_airport': flight.departure_airport,
                'arrival_airport': flight.arrival_airport,
                'departure_time': flight.departure_time,
                'arrival_time': flight.arrival_time,
                'duration': flight.duration,
                'price': flight.price,
                'flight_number': flight.flight_number
            }
            for flight in itinerary.flights
        ],
        'hotels': [
            {
                'name': hotel.name,
                'address': hotel.address,
                'city': hotel.city,
                'country': hotel.country,
                'price_per_night': hotel.price_per_night,
                'rating': hotel.rating,
                'amenities': hotel.amenities
            }
            for hotel in itinerary.hotels
        ],
        'points_of_interest': [
            {
                'name': poi.name,
                'description': poi.description,
                'category': poi.category,
                'address': poi.address,
                'city': poi.city,
                'country': poi.country,
                'rating': poi.rating,
                'price_range': poi.price_range,
                'opening_hours': poi.opening_hours
            }
            for poi in itinerary.points_of_interest
        ]
    }
    
    with open(filename, 'w') as f:
        json.dump(itinerary_dict, f, indent=2)
    
    print(f"✅ Itinerary exported to {filename}")

def main():
    """Main demo function."""
    print("🎯 Travel Itinerary Tool - Demo Mode")
    print("=" * 50)
    print("This demo shows the tool's capabilities using sample data.")
    print("No API keys required for this demonstration.\n")
    
    # Create sample itinerary
    print("📝 Creating sample itinerary...")
    itinerary = create_sample_itinerary()
    
    # Display summary
    display_itinerary_summary(itinerary)
    
    # Export to JSON
    print(f"\n📤 Exporting itinerary...")
    export_itinerary_json(itinerary)
    
    print(f"\n🎉 Demo completed successfully!")
    print(f"\nTo use the full application with real data:")
    print(f"1. Set up your API keys in the .env file")
    print(f"2. Run: python app.py")
    print(f"3. Or run: streamlit run streamlit_app.py")

if __name__ == "__main__":
    main()

