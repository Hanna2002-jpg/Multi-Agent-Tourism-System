import requests

def get_coordinates(place_name):
    """
    Fetches the latitude and longitude of a given place name using the Nominatim API.
    
    Args:
        place_name (str): The name of the place to search for.
    
    Returns:
        dict: {lat, lon, display_name, addresstype} if found, else None.
    """
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": place_name,
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "MyTourismApp/1.0" 
    }
    
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        if data:
            result = data[0]
            return {
                "lat": float(result["lat"]),
                "lon": float(result["lon"]),
                "display_name": result["display_name"],
                "addresstype": result.get("addresstype", "unknown"),
                "found": True
            }
        else:
            return None
    except requests.RequestException as e:
        print(f"Error fetching coordinates: {e}")
        return None
