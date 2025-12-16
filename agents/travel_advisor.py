
def get_packing_suggestion(weather_data):
    """
    Returns a list of packing items based on weather data.
    """
    items = []
    
    if not weather_data or isinstance(weather_data, str):
        return ["Check forecast before packing", "Comfortable walking shoes"]
    
    try:
        temp = weather_data.get('temperature', 25)
        rain = weather_data.get('rain_chance', 0)
        
        # Temperature-based
        if temp > 30:
            items.append(f"☀️ Sunscreen & sunglasses (High: {temp}°C)")
            items.append("👕 Light, breathable clothes")
            items.append("💧 Water bottle (stay hydrated!)")
        elif temp > 20:
            items.append(f"👕 Light layers (Avg: {temp}°C)")
            items.append("🧢 Cap or hat")
        else:
            items.append(f"🧥 Light jacket (Low: {temp}°C)")
            items.append("👖 Long pants")
            
        # Rain-based
        if rain > 50:
            items.append(f"☔ Umbrella (Rain chance: {rain}%)")
            items.append("👟 Waterproof shoes")
        elif rain > 20:
            items.append(f"🌂 Umbrella (just in case, {rain}% rain)")
        else:
            items.append(f"❌ No umbrella needed ({rain}% rain)")
            
        # Essentials
        items.append("👟 Comfortable walking shoes")
        items.append("📱 Phone & power bank")
        
    except AttributeError:
        items.append("Standard travel kit")
        
    return items

def get_budget_estimate(city_name, full_name=""):
    """
    Returns a budget dictionary based on city tier and region (India vs Int'l).
    """
    # Detect Region based on full name or city
    full_lower = (city_name + " " + full_name).lower()
    
    # Regions
    europe = ["italy", "france", "spain", "germany", "uk", "london", "paris", "rome", "europe"]
    us = ["usa", "united states", "new york", "california", "america"]
    
    if any(x in full_lower for x in europe):
        return {
            "Budget": "€50-70 ($55-77)",
            "Mid-range": "€100-150 ($110-165)",
            "Luxury": "€250+ ($275+)"
        }
    elif any(x in full_lower for x in us):
        return {
            "Budget": "$80-100",
            "Mid-range": "$150-250",
            "Luxury": "$400+"
        }
    
    # Default to India logic (refined)
    expensive_india = ["bangalore", "mumbai", "delhi", "goa"]
    if any(x in full_lower for x in expensive_india):
        return {
            "Budget": "₹2000-3000 ($24-36)",
            "Mid-range": "₹4000-6000 ($48-72)",
            "Luxury": "₹10000+ ($120+)"
        }
    else:
        # Tier 2 India
        return {
            "Budget": "₹1000-2000 ($12-24)",
            "Mid-range": "₹2500-4000 ($30-48)",
            "Luxury": "₹7000+ ($84+)"
        }

def get_travel_tips(city_name):
    """
    Returns specific travel tips for supported cities or generic ones.
    """
    tips = {
        "kochi": [
            "Best time: Nov-Feb (cooler)",
            "Try 'Sadya' on banana leaf",
            "Ferry is the best transport"
        ],
        "bangalore": [
            "Uber/Ola is better than auto-Rickshaws",
            "Traffic is heavy - use Metro",
            "Visit breweries in Indiranagar"
        ],
        "rome": [
            "Buy a 'Roma Pass' for transport & museums",
            "Don't order cappuccino after 11 AM (local custom)",
            "Watch for pickpockets at Trevi Fountain"
        ],
        "paris": [
            "Learn basic French greetings (Bonjour/Merci)",
            "Metro is the fastest way around",
            "Dinner starts late (8 PM+)"
        ],
        "new york": [
            "Get a MetroCard for subways",
            "Pizza slices are the best cheap eat",
            "Walk across Brooklyn Bridge"
        ]
    }
    
    city_lower = city_name.lower()
    for key, val in tips.items():
        if key in city_lower:
            return val
            
    return [
        "Check local transport apps",
        "Keep cash for small purchases",
        "Download offline maps",
        "Try local street food"
    ]

def get_activity_advice(weather_data):
    """
    Returns advice based on weather conditions.
    """
    if not weather_data or isinstance(weather_data, str):
        return "Check local forecast to plan your day."
    
    try:
        rain = weather_data.get('rain_chance', 0)
        temp = weather_data.get('temperature', 25)
        
        if rain > 40:
            return "🌧️ Rainy conditions expected. Great time for museums, art galleries, or cafe hopping!"
        elif temp < 15:
            return "🧊 Cool weather - great for museums and indoor attractions."
        elif 15 <= temp < 25:
            return "☀️ Pleasant weather for outdoor activities! Visit parks and monuments."
        else: # temp >= 25
            return "🌡️ Warm weather - perfect for exploring, stay hydrated!"
    except AttributeError:
        return "Enjoy your day!"
