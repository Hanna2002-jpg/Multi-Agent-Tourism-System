# Multi-Agent-Tourism-System
An intelligent AI-powered travel planning assistant that orchestrates multiple specialized agents to provide comprehensive trip information including real-time weather, tourist attractions, packing suggestions, and local tips.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Examples](#examples)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This multi-agent tourism system helps travelers plan their trips by providing:
- Real-time weather information
- Top tourist attractions
- Smart packing recommendations
- City-specific travel tips

The system uses a parent-child agent architecture where a Tourism AI Agent orchestrates specialized child agents (Weather Agent and Places Agent) to gather and process information from multiple APIs.

## ✨ Features

### Core Features (Assignment Requirements)
- 🤖 **Parent Agent**: Tourism AI Agent orchestrating the entire system
- 🌤️ **Weather Agent**: Fetches current weather and forecasts using Open-Meteo API
- 📍 **Places Agent**: Suggests up to 5 tourist attractions using Overpass & Nominatim APIs
- ⚠️ **Error Handling**: Smart handling of non-existent places with helpful suggestions

### Enhanced Features (Beyond Requirements)
- 🧠 **Intelligent Weather Interpretation**: Context-aware activity recommendations based on temperature
- 🎒 **Dynamic Packing Suggestions**: Temperature and rain-based clothing recommendations
- 🗺️ **Geographic Intelligence**: Handles countries, states, regions, and cities
- 💡 **City-Specific Pro Tips**: Localized travel advice for major destinations
- 🔄 **Context-Aware Conversations**: Natural follow-up question handling
- 🎨 **Beautiful UI**: Emoji-based formatting for enhanced readability

## 🏗️ System Architecture

```
User Input
    ↓
Tourism AI Agent (Parent)
    ↓
    ├─→ Weather Agent → Open-Meteo API
    │        ↓
    │   Weather Data
    │
    └─→ Places Agent → Nominatim API → Overpass API
             ↓
        Tourist Attractions
             ↓
    ┌────────┴────────┐
    ↓                 ↓
Weather            Packing
Interpretation     Suggestions
    ↓                 ↓
    └────────┬────────┘
             ↓
    City-Specific Tips
             ↓
    Formatted Response
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/multi-agent-tourism-system.git
cd multi-agent-tourism-system
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python main.py
```

## 💻 Usage

### Basic Usage

Start the application and enter your destination:

```bash
$ python main.py
Multi-Agent Tourism System Initialized.
How can I help you? (e.g., 'I'm going to go to Bangalore, let's plan my trip')
> I'm travelling to Paris
```

### Supported Query Types

1. **Simple city queries**
   ```
   > Paris
   > Bangalore
   > Tokyo
   ```

2. **Natural language queries**
   ```
   > I'm travelling to Bangalore. Help me plan this.
   > What's the weather in Paris?
   > I'm going to Kochi, let's plan my trip
   ```

3. **Country/State queries**
   ```
   > France
   → Suggests: Paris, Nice, Lyon
   
   > Rajasthan
   → Suggests: Jaipur, Udaipur, Jodhpur, Jaisalmer
   ```

## 📡 API Documentation

### APIs Used

#### 1. Open-Meteo API (Weather)
- **Endpoint**: `https://api.open-meteo.com/v1/forecast`
- **Purpose**: Real-time weather data and forecasts
- **Documentation**: https://open-meteo.com/en/docs
- **Rate Limit**: Free tier available

#### 2. Nominatim API (Geocoding)
- **Endpoint**: `https://nominatim.openstreetmap.org/search`
- **Purpose**: Convert place names to coordinates
- **Documentation**: https://nominatim.org/release-docs/develop/api/Search/
- **Rate Limit**: 1 request per second

#### 3. Overpass API (Places)
- **Endpoint**: `https://overpass-api.de/api/interpreter`
- **Purpose**: Fetch tourist attractions from OpenStreetMap
- **Documentation**: https://wiki.openstreetmap.org/wiki/Overpass_API
- **Rate Limit**: Fair use policy

## 📖 Examples

### Example 1: Bangalore Query

**Input:**
```
> I'm travelling to Bangalore. Help me plan this.
```

**Output:**
```
🌤️ Weather in Bengaluru:
Currently 20.3°C (Overcast) with 3% chance of rain.
☀️ Pleasant weather for outdoor activities! Visit parks and monuments.

📍 Top Places to Visit:
1. Queen Victoria
2. Lalbagh Botanical Gardens
3. Cubbon Park
4. Freedom Park
5. Tippu's Summer Palace

🎒 What to Pack:
- 👕 Light layers (Avg: 20.3°C)
- 🧢 Cap or hat
- ❌ No umbrella needed (3% rain)
- 👟 Comfortable walking shoes
- 📱 Phone & power bank

💡 Pro Tips:
- Check local transport apps
- Keep cash for small purchases
- Download offline maps
- Try local street food
```

### Example 2: Paris Query

**Input:**
```
> Paris
```

**Output:**
```
🌤️ Weather in Paris:
Currently 13.6°C (Overcast) with 3% chance of rain.
🧊 Cool weather - great for museums and indoor attractions.

📍 Top Places to Visit:
1. Musée de l'Armée
2. Point zéro des Routes de France
3. Musée des Arts Décoratifs
4. Musée des Arts et Métiers
5. Tour de Jean-sans-Peur

🎒 What to Pack:
- 🧥 Light jacket (Low: 13.6°C)
- 👖 Long pants
- ❌ No umbrella needed (3% rain)
- 👟 Comfortable walking shoes
- 📱 Phone & power bank

💡 Pro Tips:
- Learn basic French greetings (Bonjour/Merci)
- Metro is the fastest way around
- Dinner starts late (8 PM+)
```

### Example 3: State/Country Query

**Input:**
```
> Rajasthan
```

**Output:**
```
'Rajasthan, India' is a state. Please specify a city for better recommendations.
Popular cities include: Jaipur, Udaipur, Jodhpur, Jaisalmer.
```

## 🛠️ Technologies Used

- **Language**: Python 3.8+
- **APIs**: 
  - Open-Meteo API (Weather data)
  - Nominatim API (Geocoding)
  - Overpass API (Places/Tourism)
- **Architecture**: Multi-Agent System
- **Key Libraries**:
  - `requests` - API calls
  - `json` - Data handling
  - Custom agent implementations

## 📁 Project Structure

```
multi-agent-tourism-system/
│
├── main.py                 # Main application entry point
├── agents/
│   ├── parent_agent.py     # Tourism AI orchestrator
│   ├── weather_agent.py    # Weather data agent
│   └── places_agent.py     # Places discovery agent
│
├── utils/
│   ├── api_handler.py      # API request handling
│   └── formatter.py        # Output formatting
│
├── config/
│   └── config.py           # Configuration settings
│
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── LICENSE                # License information
```

## 🎨 Features Breakdown

### Weather Intelligence
- **Temperature Interpretation**: Different recommendations for different climates
  - < 15°C: Museums and indoor attractions
  - 15-25°C: Outdoor activities
  - > 25°C: Outdoor exploration with hydration tips

### Smart Packing
- **Temperature-based**:
  - Cold: Jacket, long pants, scarf
  - Moderate: Light layers
  - Warm: Light clothes, cap, sunscreen
- **Rain-based**:
  - < 20% rain: No umbrella
  - > 30% rain: Umbrella recommended

### Geographic Handling
- Countries → City suggestions
- States → City suggestions within state
- Cities → Direct information
- Regions → Specific location requests

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Future Enhancements

- [ ] Multi-day itinerary planning
- [ ] Restaurant recommendations
- [ ] Hotel suggestions with pricing
- [ ] Flight search integration
- [ ] Budget breakdown by activity
- [ ] Real events API integration (Predicthq/Eventbrite)
- [ ] User preferences and history
- [ ] Multi-language support

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


⭐ Star this repo if you find it helpful!
```
