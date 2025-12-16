import requests

def get_places(lat, lon):
    """
    Fetches major tourist attractions near a given latitude and longitude using Overpass API.
    Uses 'nwr' (node, way, relation) to capture large places like parks and museums.
    """
    overpass_url = "https://overpass-api.de/api/interpreter"
    
    # Strategy:
    # 1. Try Strict Query (High Quality: has wikipedia tag)
    # 2. If < 3 results, Try Broad Query (Any named tourism attraction)
    
    strict_query = f"""
    [out:json][timeout:25];
    (
      nwr["tourism"~"attraction|museum|zoo|theme_park|aquarium|viewpoint"]["name"]["wikipedia"](around:5000, {lat}, {lon});
      nwr["historic"~"castle|monument|memorial|ruins"]["name"]["wikipedia"](around:5000, {lat}, {lon});
      nwr["leisure"="park"]["name"]["wikipedia"](around:5000, {lat}, {lon});
    );
    out center body; 
    """
    
    broad_query = f"""
    [out:json][timeout:25];
    (
      nwr["tourism"~"attraction|museum|zoo|theme_park|aquarium|viewpoint"]["name"](around:5000, {lat}, {lon});
      nwr["historic"~"castle|monument|memorial|ruins"]["name"](around:5000, {lat}, {lon});
      nwr["leisure"="park"]["name"](around:5000, {lat}, {lon});
    );
    out center body; 
    """

    def fetch_overpass(query):
        try:
            response = requests.post(overpass_url, data=query)
            response.raise_for_status()
            data = response.json()
            items = []
            seen = set()
            for element in data.get("elements", []):
                tags = element.get("tags", {})
                name = tags.get("name")
                if name and name not in seen:
                    items.append(name)
                    seen.add(name)
            return items
        except Exception as e:
            print(f"Overpass Error: {e}")
            return []

    # 1. Strict
    places = fetch_overpass(strict_query)
    
    # 2. Fallback if needed
    if len(places) < 3:
        # print("DEBUG: Not enough strict results, trying broad query...")
        more_places = fetch_overpass(broad_query)
        # Append unique new places
        for p in more_places:
            if p not in places:
                places.append(p)
                
    return places[:5]
