from agents.orchestrator import TourismAgent

def main():
    agent = TourismAgent()
    
    print("Multi-Agent Tourism System Initialized.")
    print("How can I help you? (e.g., 'I'm going to go to Bangalore, let's plan my trip')")
    
    while True:
        user_input = input("\n> ")
        if user_input.lower() in ['exit', 'quit']:
            break
        
        result = agent.process_request(user_input)
        
        if "error" in result:
            print(result["error"])
        else:
            city = result['city']
            intents = result.get('intents', {})
            
            # 1. Weather Section
            print(f"\n🌤️ Weather in {city}:")
            if result['weather'] and "error" not in result['weather']:
                w = result['weather']
                print(f"Currently {w['temperature']}°C ({w['description']}) with {w['rain_chance']}% chance of rain.")
                adv = result.get('activity_advice')
                if adv:
                    print(adv)
            else:
                print("Weather data unavailable.")

            # 2. Places Section
            if intents.get('places') or True: # Always show places for "Plan my trip" type queries
                print(f"\n📍 Top Places to Visit:")
                places = result['places']
                if places:
                    for i, p in enumerate(places, 1):
                        print(f"{i}. {p}")
                else:
                    print("Could not find specific attractions.")

            # 3. Packing Section
            print(f"\n🎒 What to Pack:")
            for item in result.get('packing', []):
                print(f"- {item}")

            # 4. Tips Section
            print(f"\n💡 Pro Tips:")
            for tip in result.get('tips', []):
                print(f"- {tip}")
                     
if __name__ == "__main__":
    main()
