"""
LLM service for generating travel itineraries using OpenAI.
"""
import json
from datetime import datetime, date, timedelta
from typing import List, Dict, Any, Optional
from openai import OpenAI
from config import Config
from models import TravelItinerary, DayItinerary, Flight, Hotel, PointOfInterest

class ItineraryGenerator:
    """Service for generating travel itineraries using LLM."""
    
    def __init__(self):
        self.client = OpenAI(api_key=Config.get_api_key('openai'))
        self.model = "gpt-3.5-turbo"
    
    def generate_itinerary(self, destination: str, start_date: str, end_date: str,
                          budget: float, travelers: int, preferences: Dict[str, Any],
                          travel_data: Dict[str, Any]) -> TravelItinerary:
        """Generate a comprehensive travel itinerary."""
        
        # Calculate duration
        start = datetime.strptime(start_date, "%Y-%m-%d").date()
        end = datetime.strptime(end_date, "%Y-%m-%d").date()
        duration = (end - start).days
        
        # Prepare context for LLM
        context = self._prepare_context(destination, start_date, end_date, budget, 
                                      travelers, preferences, travel_data)
        
        # Generate itinerary using LLM
        itinerary_data = self._call_llm(context)
        
        # Parse and structure the response
        itinerary = self._parse_itinerary_response(itinerary_data, destination, 
                                                 start, end, budget, travelers)
        
        return itinerary
    
    def _prepare_context(self, destination: str, start_date: str, end_date: str,
                        budget: float, travelers: int, preferences: Dict[str, Any],
                        travel_data: Dict[str, Any]) -> str:
        """Prepare context for LLM prompt."""
        
        context = f"""
        Generate a detailed travel itinerary for {travelers} traveler(s) visiting {destination}
        from {start_date} to {end_date} with a budget of ${budget}.
        
        Traveler Preferences:
        - Interests: {preferences.get('interests', 'General sightseeing')}
        - Travel Style: {preferences.get('travel_style', 'Balanced')}
        - Food Preferences: {preferences.get('food_preferences', 'Open to local cuisine')}
        - Activity Level: {preferences.get('activity_level', 'Moderate')}
        
        Available Data:
        """
        
        # Add flight information
        if travel_data.get('flights'):
            context += "\n\nFlight Options:\n"
            for i, flight in enumerate(travel_data['flights'][:5], 1):
                context += f"{i}. {flight.get('airline', 'Unknown')} - {flight.get('description', 'No description')}\n"
        
        # Add hotel information
        if travel_data.get('hotels'):
            context += "\n\nHotel Options:\n"
            for i, hotel in enumerate(travel_data['hotels'][:5], 1):
                context += f"{i}. {hotel.get('name', 'Unknown')} - {hotel.get('description', 'No description')}\n"
        
        # Add POI information
        if travel_data.get('pois'):
            context += "\n\nPoints of Interest:\n"
            for i, poi in enumerate(travel_data['pois'][:10], 1):
                context += f"{i}. {poi.get('name', 'Unknown')} - {poi.get('description', 'No description')}\n"
        
        context += f"""
        
        Please generate a day-by-day itinerary that includes:
        1. Daily activities and attractions
        2. Meal recommendations (breakfast, lunch, dinner)
        3. Transportation between locations
        4. Estimated costs for each day
        5. Time allocations for each activity
        6. Practical tips and recommendations
        
        Format the response as a JSON object with the following structure:
        {{
            "itinerary": {{
                "destination": "{destination}",
                "start_date": "{start_date}",
                "end_date": "{end_date}",
                "budget": {budget},
                "travelers": {travelers},
                "days": [
                    {{
                        "date": "YYYY-MM-DD",
                        "city": "City Name",
                        "activities": [
                            {{
                                "time": "HH:MM",
                                "activity": "Activity Name",
                                "description": "Detailed description",
                                "duration": "X hours",
                                "cost": 0.0,
                                "location": "Address or area"
                            }}
                        ],
                        "meals": [
                            {{
                                "time": "HH:MM",
                                "meal": "Meal Type",
                                "restaurant": "Restaurant Name",
                                "description": "Description",
                                "cost": 0.0,
                                "location": "Address"
                            }}
                        ],
                        "transportation": [
                            {{
                                "from": "Starting location",
                                "to": "Destination",
                                "method": "Transportation method",
                                "cost": 0.0,
                                "duration": "X minutes"
                            }}
                        ],
                        "daily_budget": 0.0,
                        "tips": "Daily tips and recommendations"
                    }}
                ]
            }}
        }}
        """
        
        return context
    
    def _call_llm(self, context: str) -> Dict[str, Any]:
        """Call OpenAI API to generate itinerary."""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert travel planner. Generate detailed, practical, and engaging travel itineraries. Always respond with valid JSON format."
                    },
                    {
                        "role": "user",
                        "content": context
                    }
                ],
                max_tokens=4000,
                temperature=0.7
            )
            
            content = response.choices[0].message.content
            
            # Try to extract JSON from the response
            try:
                # Look for JSON in the response
                start_idx = content.find('{')
                end_idx = content.rfind('}') + 1
                if start_idx != -1 and end_idx != 0:
                    json_str = content[start_idx:end_idx]
                    return json.loads(json_str)
                else:
                    raise ValueError("No JSON found in response")
            except (json.JSONDecodeError, ValueError) as e:
                print(f"Error parsing LLM response: {e}")
                # Return a fallback structure
                return self._create_fallback_itinerary()
                
        except Exception as e:
            print(f"Error calling LLM: {e}")
            return self._create_fallback_itinerary()
    
    def _create_fallback_itinerary(self) -> Dict[str, Any]:
        """Create a fallback itinerary when LLM fails."""
        return {
            "itinerary": {
                "destination": "Destination",
                "start_date": "2024-01-01",
                "end_date": "2024-01-03",
                "budget": 1000,
                "travelers": 1,
                "days": [
                    {
                        "date": "2024-01-01",
                        "city": "Destination City",
                        "activities": [
                            {
                                "time": "09:00",
                                "activity": "City Tour",
                                "description": "Explore the main attractions of the city",
                                "duration": "3 hours",
                                "cost": 50.0,
                                "location": "City Center"
                            }
                        ],
                        "meals": [
                            {
                                "time": "12:00",
                                "meal": "Lunch",
                                "restaurant": "Local Restaurant",
                                "description": "Try local cuisine",
                                "cost": 25.0,
                                "location": "City Center"
                            }
                        ],
                        "transportation": [],
                        "daily_budget": 75.0,
                        "tips": "Wear comfortable walking shoes"
                    }
                ]
            }
        }
    
    def _parse_itinerary_response(self, data: Dict[str, Any], destination: str,
                                 start_date: date, end_date: date, budget: float,
                                 travelers: int) -> TravelItinerary:
        """Parse LLM response into TravelItinerary object."""
        
        itinerary_data = data.get('itinerary', {})
        days_data = itinerary_data.get('days', [])
        
        # Create day itineraries
        days = []
        current_date = start_date
        
        for day_data in days_data:
            day_itinerary = DayItinerary(
                date=current_date,
                city=day_data.get('city', destination),
                activities=day_data.get('activities', []),
                meals=day_data.get('meals', []),
                transportation=day_data.get('transportation', [])
            )
            days.append(day_itinerary)
            current_date += timedelta(days=1)
        
        # Create main itinerary
        itinerary = TravelItinerary(
            destination=destination,
            start_date=start_date,
            end_date=end_date,
            duration_days=(end_date - start_date).days,
            budget=budget,
            travelers=travelers,
            days=days
        )
        
        return itinerary
    
    def enhance_itinerary(self, itinerary: TravelItinerary, 
                         additional_preferences: Dict[str, Any]) -> TravelItinerary:
        """Enhance an existing itinerary with additional preferences."""
        
        # This could be used to refine or modify an existing itinerary
        # For now, we'll return the original itinerary
        return itinerary
    
    def generate_summary(self, itinerary: TravelItinerary) -> str:
        """Generate a summary of the itinerary."""
        
        summary = f"""
        Travel Itinerary Summary
        ========================
        
        Destination: {itinerary.destination}
        Duration: {itinerary.duration_days} days
        Travelers: {itinerary.travelers}
        Budget: ${itinerary.budget}
        
        Daily Breakdown:
        """
        
        for i, day in enumerate(itinerary.days, 1):
            summary += f"\nDay {i} ({day.date}):\n"
            summary += f"  City: {day.city}\n"
            summary += f"  Activities: {len(day.activities)} planned\n"
            summary += f"  Meals: {len(day.meals)} planned\n"
            if day.transportation:
                summary += f"  Transportation: {len(day.transportation)} segments\n"
        
        return summary

