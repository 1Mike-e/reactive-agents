# Simulated local weather dataset
weather_data = {
    "new york": "☁️ Cloudy, 58°F",
    "los angeles": "☀️ Sunny, 75°F",
    "chicago": "🌧️ Rainy, 60°F",
    "atlanta": "⛅ Partly cloudy, 70°F",
    "boston": "🌬️ Windy, 55°F"
}

def weather_responder(query: str) -> str:
    weather_data = {
        "new york": "☁️ Cloudy, 58°F",
        "los angeles": "☀️ Sunny, 75°F",
        "chicago": "🌧️ Rainy, 60°F",
        "atlanta": "⛅ Partly cloudy, 70°F",
        "boston": "🌬️ Windy, 55°F"
    }
 
    query_lower = query.lower()
    
    for city in weather_data:
        if city in query_lower:
            return f"The weather in {city.title()} is: {weather_data[city]}"
    
    return "Sorry, I don't have weather data for that location."
 
# 🧪 Test
print(weather_responder("What's the weather like in Chicago?"))
print(weather_responder("Tell me the weather in Los Angeles."))
print(weather_responder("Do you know the forecast for Miami?"))