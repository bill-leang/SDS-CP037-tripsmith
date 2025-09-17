"""
API clients for fetching travel data from various sources.
"""
import requests
import json
from typing import List, Dict, Any, Optional
from tavily import TavilyClient
from serpapi import GoogleSearch
from config import Config
from models import Flight, Hotel, PointOfInterest

class TavilyAPIClient:
    """Client for Tavily search API."""
    
    def __init__(self):
        self.client = TavilyClient(api_key=Config.get_api_key('tavily'))
    
    def search_flights(self, origin: str, destination: str, departure_date: str, 
                      return_date: Optional[str] = None, passengers: int = 1) -> List[Dict[str, Any]]:
        """Search for flights using Tavily."""
        query = f"flights from {origin} to {destination} on {departure_date}"
        if return_date:
            query += f" return {return_date}"
        
        try:
            response = self.client.search(
                query=query,
                search_depth="advanced",
                max_results=10
            )
            return self._parse_flight_results(response.get('results', []))
        except Exception as e:
            print(f"Error searching flights: {e}")
            return []
    
    def search_hotels(self, city: str, check_in: str, check_out: str, 
                     guests: int = 1) -> List[Dict[str, Any]]:
        """Search for hotels using Tavily."""
        query = f"hotels in {city} check in {check_in} check out {check_out} {guests} guests"
        
        try:
            response = self.client.search(
                query=query,
                search_depth="advanced",
                max_results=10
            )
            return self._parse_hotel_results(response.get('results', []))
        except Exception as e:
            print(f"Error searching hotels: {e}")
            return []
    
    def search_pois(self, city: str, category: str = "attractions") -> List[Dict[str, Any]]:
        """Search for points of interest using Tavily."""
        query = f"{category} in {city} tourist attractions things to do"
        
        try:
            response = self.client.search(
                query=query,
                search_depth="advanced",
                max_results=15
            )
            return self._parse_poi_results(response.get('results', []))
        except Exception as e:
            print(f"Error searching POIs: {e}")
            return []
    
    def _parse_flight_results(self, results: List[Dict]) -> List[Dict[str, Any]]:
        """Parse flight search results."""
        flights = []
        for result in results:
            # This is a simplified parser - in reality, you'd need more sophisticated parsing
            flights.append({
                'airline': result.get('title', 'Unknown'),
                'description': result.get('content', ''),
                'url': result.get('url', ''),
                'published_date': result.get('published_date', '')
            })
        return flights
    
    def _parse_hotel_results(self, results: List[Dict]) -> List[Dict[str, Any]]:
        """Parse hotel search results."""
        hotels = []
        for result in results:
            hotels.append({
                'name': result.get('title', 'Unknown'),
                'description': result.get('content', ''),
                'url': result.get('url', ''),
                'published_date': result.get('published_date', '')
            })
        return hotels
    
    def _parse_poi_results(self, results: List[Dict]) -> List[Dict[str, Any]]:
        """Parse POI search results."""
        pois = []
        for result in results:
            pois.append({
                'name': result.get('title', 'Unknown'),
                'description': result.get('content', ''),
                'url': result.get('url', ''),
                'published_date': result.get('published_date', '')
            })
        return pois

class SerpAPIClient:
    """Client for SerpAPI (Google Search API)."""
    
    def __init__(self):
        self.api_key = Config.get_api_key('serpapi')
    
    def search_flights(self, origin: str, destination: str, departure_date: str,
                      return_date: Optional[str] = None, passengers: int = 1) -> List[Dict[str, Any]]:
        """Search for flights using SerpAPI."""
        params = {
            "engine": "google_flights",
            "departure_id": origin,
            "arrival_id": destination,
            "outbound_date": departure_date,
            "api_key": self.api_key
        }
        
        if return_date:
            params["return_date"] = return_date
        
        try:
            search = GoogleSearch(params)
            results = search.get_dict()
            return self._parse_flight_results(results)
        except Exception as e:
            print(f"Error searching flights with SerpAPI: {e}")
            return []
    
    def search_hotels(self, city: str, check_in: str, check_out: str,
                     guests: int = 1) -> List[Dict[str, Any]]:
        """Search for hotels using SerpAPI."""
        params = {
            "engine": "google_hotels",
            "q": f"hotels in {city}",
            "checkin_date": check_in,
            "checkout_date": check_out,
            "adults": guests,
            "api_key": self.api_key
        }
        
        try:
            search = GoogleSearch(params)
            results = search.get_dict()
            return self._parse_hotel_results(results)
        except Exception as e:
            print(f"Error searching hotels with SerpAPI: {e}")
            return []
    
    def search_pois(self, city: str, category: str = "attractions") -> List[Dict[str, Any]]:
        """Search for points of interest using SerpAPI."""
        params = {
            "engine": "google",
            "q": f"{category} in {city} tourist attractions",
            "api_key": self.api_key
        }
        
        try:
            search = GoogleSearch(params)
            results = search.get_dict()
            return self._parse_poi_results(results)
        except Exception as e:
            print(f"Error searching POIs with SerpAPI: {e}")
            return []
    
    def _parse_flight_results(self, results: Dict) -> List[Dict[str, Any]]:
        """Parse SerpAPI flight results."""
        flights = []
        flight_results = results.get('flights', {}).get('options', [])
        
        for flight in flight_results:
            flights.append({
                'airline': flight.get('airline', 'Unknown'),
                'departure_time': flight.get('departure_time', ''),
                'arrival_time': flight.get('arrival_time', ''),
                'price': flight.get('price', 0),
                'duration': flight.get('duration', ''),
                'stops': flight.get('stops', 0)
            })
        
        return flights
    
    def _parse_hotel_results(self, results: Dict) -> List[Dict[str, Any]]:
        """Parse SerpAPI hotel results."""
        hotels = []
        hotel_results = results.get('hotels', {}).get('results', [])
        
        for hotel in hotel_results:
            hotels.append({
                'name': hotel.get('name', 'Unknown'),
                'price': hotel.get('price', 0),
                'rating': hotel.get('rating', 0),
                'address': hotel.get('address', ''),
                'amenities': hotel.get('amenities', [])
            })
        
        return hotels
    
    def _parse_poi_results(self, results: Dict) -> List[Dict[str, Any]]:
        """Parse SerpAPI POI results."""
        pois = []
        organic_results = results.get('organic_results', [])
        
        for result in organic_results:
            pois.append({
                'name': result.get('title', 'Unknown'),
                'description': result.get('snippet', ''),
                'url': result.get('link', ''),
                'rating': result.get('rating', 0)
            })
        
        return pois

class TravelDataFetcher:
    """Main class for fetching travel data from multiple sources."""
    
    def __init__(self):
        self.tavily_client = TavilyAPIClient()
        self.serpapi_client = SerpAPIClient()
    
    def get_comprehensive_data(self, destination: str, start_date: str, end_date: str,
                             origin: str = None, budget: float = 1000) -> Dict[str, Any]:
        """Fetch comprehensive travel data from multiple sources."""
        data = {
            'flights': [],
            'hotels': [],
            'pois': []
        }
        
        # Fetch flights if origin is provided
        if origin:
            try:
                data['flights'].extend(self.tavily_client.search_flights(origin, destination, start_date, end_date))
                data['flights'].extend(self.serpapi_client.search_flights(origin, destination, start_date, end_date))
            except Exception as e:
                print(f"Error fetching flights: {e}")
        
        # Fetch hotels
        try:
            data['hotels'].extend(self.tavily_client.search_hotels(destination, start_date, end_date))
            data['hotels'].extend(self.serpapi_client.search_hotels(destination, start_date, end_date))
        except Exception as e:
            print(f"Error fetching hotels: {e}")
        
        # Fetch points of interest
        try:
            data['pois'].extend(self.tavily_client.search_pois(destination))
            data['pois'].extend(self.serpapi_client.search_pois(destination))
        except Exception as e:
            print(f"Error fetching POIs: {e}")
        
        return data
