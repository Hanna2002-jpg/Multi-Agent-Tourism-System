import requests
from datetime import datetime

WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Fog", 48: "Depositing rime fog",
    51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
    61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
    71: "Slight snow fall", 73: "Moderate snow fall", 75: "Heavy snow fall",
    77: "Snow grains",
    80: "Slight rain showers", 81: "Moderate rain showers", 82: "Violent rain showers",
    85: "Slight snow showers", 86: "Heavy snow showers",
    95: "Thunderstorm", 96: "Thunderstorm with slight hail", 99: "Thunderstorm with heavy hail"
}

def get_weather(lat, lon):
    """
    Fetches the current weather and precipitation chance using Open-Meteo API.
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": "true",
        "hourly": "precipitation_probability", # Needed for chance of rain
        "timezone": "auto"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        # 1. Current Weather
        cw = data.get("current_weather", {})
        temp = cw.get("temperature", "N/A")
        code = cw.get("weathercode", 0)
        desc = WEATHER_CODES.get(code, "Unknown weather")
        
        # 2. Precipitation Probability
        # Open-Meteo returns hourly data list. We need to find the current hour's index.
        # Simple approximation: take the first hour (current time) or 0 index
        rain_chance = 0
        if "hourly" in data and "precipitation_probability" in data["hourly"]:
            # 'time' list in hourly corresponds to 'precipitation_probability' list
            # We'll just grab the current probability (index 0 is usually the start of the requested time or 'now')
            # For more precision we could parse timestamps, but 0 index is 'current hour' in standard request
            current_hour_index = datetime.now().hour 
            # Note: The API returns 24h forecast for today starting at 00:00. 
            # If request is made at 8 PM, index 20 is the current hour.
            # However, safer to just assume the current 'current_weather' matches the 'now' time.
            # Let's find index by matching current hour.
            
            # Simple fallback: use the first value if parsing fails
            try:
                rain_chance = data["hourly"]["precipitation_probability"][datetime.now().hour]
            except:
                rain_chance = data["hourly"]["precipitation_probability"][0]

        return {
            "temperature": temp,
            "description": desc,
            "rain_chance": rain_chance
        }
            
    except requests.RequestException as e:
        return {"error": f"Failed to fetch weather: {e}"}
