import re
from utils.geocoding import get_coordinates
from agents.weather_agent import get_weather
from agents.places_agent import get_places
from agents.travel_advisor import get_packing_suggestion, get_travel_tips, get_activity_advice

class TourismAgent:
    def __init__(self):
        pass

    def extract_location(self, query):
        """
        Extracts location from query using regex patterns or loose matching.
        """
    def extract_location(self, text):
        """
        Extracts location from query using robust regex patterns and cleaning.
        """
        # Clean punctuation at sentence boundaries
        text = re.sub(r'[.!?]+\s+', ' ', text)
        
        # Patterns to extract location
        # Matches: "going to X", "visit X", "trip to X", "traveling to X"
        # Stops at: punctuation, end of string, or keywords (help, plan, etc.)
        patterns = [
            r"(?:going|go|visit\w*|travel\w*|trip)\s+(?:to\s+)?([a-zA-Z\s]+?)(?:\s+(?:let|help|plan|what|and|please|can|could|would|me|give|tell|show)|[\.,!\?]|$)",
            r"(?:in|at)\s+([a-zA-Z\s]+?)(?:\s+(?:let|help|plan|what|and|please|can|could|would|me|give|tell|show)|[\.,!\?]|$)"
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                location = match.group(1).strip()
                
                # Secondary cleanup: Remove any trailing stop words that might have slipped into the capture group
                # (Though the regex lookahead should catch most)
                stop_words = ['help', 'plan', 'let', 'the', 'my', 'this', 'trip', 'me', 'please', 'is', 'a', 'an', 'give', 'tell', 'show']
                words = location.split()
                cleaned = []
                for word in words:
                    if word.lower() in stop_words:
                        break
                    cleaned.append(word)
                
                if cleaned:
                    return ' '.join(cleaned).strip().title()
        
        # Fallback for simple "Bangalore" type queries
        # If short query and not matched yet, assume it's the location
        # But filter common junk
        clean_text = text.lower()
        junk = ["i'm", "i", "am", "travel", "to", "city", "place", "location"]
        
        if len(text.split()) <= 3:
             # Remove junk (whole words only)
             for j in junk:
                 clean_text = re.sub(r'\b' + re.escape(j) + r'\b', '', clean_text)
             return clean_text.strip().title()

        return None

    def process_request(self, query):
        query_lower = query.lower()
        
        # 1. Detect Intents
        show_weather = False
        show_places = False
        
        if any(k in query_lower for k in ["weather", "temperature", "rain", "forecast", "hot", "cold"]):
            show_weather = True
        
        if any(k in query_lower for k in ["place", "visit", "attraction", "sight", "see", "plan"]):
            show_places = True
            
        if not show_weather and not show_places:
            show_places = True
            
        # Duration Parsing
        num_days = 1
        day_match = re.search(r"(\d+)\s*days?", query, re.IGNORECASE)
        if day_match:
            try:
                num_days = int(day_match.group(1))
            except ValueError:
                num_days = 1
            
        # 2. Extract Location
        location = self.extract_location(query)
        if not location:
            # Last ditch attempt: use raw query if short enough (likely just a city name)
            if len(query.split()) <= 3:
                location = query
            else:
                return {"error": "I couldn't identify the location."}
        
        # 3. Geocoding
        geo_result = get_coordinates(location)
        if not geo_result:
            return {"error": f"I don't know where '{location}' is."}
        
        # Geographic Level Check
        # If Country/State, ask for city.
        addr_type = geo_result.get("addresstype", "unknown")
        if addr_type in ["country", "state", "region", "province"]:
             msg = f"'{geo_result['display_name']}' is a {addr_type}. Please specify a city for better recommendations."
             
             # Suggestions for popular inputs
             suggestions = {
                 "Kerala": "Kochi, Munnar, Alappuzha, Thiruvananthapuram",
                 "Italy": "Rome, Venice, Florence, Milan",
                 "India": "Delhi, Mumbai, Jaipur, Bangalore",
                 "Karnataka": "Bangalore, Mysore, Hampi, Coorg",
                 "France": "Paris, Nice, Lyon"
             }
             
             # Check if any key in suggestions is in the display name
             for key, val in suggestions.items():
                 if key in geo_result['display_name']:
                     msg += f"\nPopular cities include: {val}."
                     break
                     
             return {"error": msg}

        lat = geo_result["lat"]
        lon = geo_result["lon"]
        display_name = geo_result["display_name"]
        simple_name = display_name.split(",")[0]
        
        result = {
            "city": simple_name,
            "full_name": display_name,
            "days": num_days,
            "intents": {
                "weather": show_weather,
                "places": show_places
            },
            "weather": None,
            "places": None
        }
        
        # 4. Execute Intended Actions
        # Always fetch weather as it drives other features
        result["weather"] = get_weather(lat, lon)
            
        if show_places:
            result["places"] = get_places(lat, lon)

        # 5. Get Advanced Features (Always fetch if we have a city, as they add value)
        # Pass the weather data (if any) to travel advisor
        weather_data = result.get("weather")
        
        result["packing"] = get_packing_suggestion(weather_data)
        result["tips"] = get_travel_tips(simple_name)
        result["activity_advice"] = get_activity_advice(weather_data)
        
        return result
