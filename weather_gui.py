import tkinter as tk
import requests

API_KEY = "e08d2ba26ac2888c4dec15d5d7d2ab9d"

def get_weather():
    city = city_entry.get().strip()

    if not city:
        result.config(text="Please enter a city name")
        return

    try:
        # Geocoding API
        geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
        geo_response = requests.get(geo_url)
        geo_data = geo_response.json()

        if not geo_data:
            result.config(text="Location not found")
            return

        lat = geo_data[0]["lat"]
        lon = geo_data[0]["lon"]
        location_name = geo_data[0]["name"]
        country = geo_data[0]["country"]

        # Weather API
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()

        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        weather = weather_data["weather"][0]["description"]
        wind_speed = weather_data["wind"]["speed"]

        result.config(
            text=f"""
📍 {location_name}, {country}

🌡 Temperature: {temperature} °C

💧 Humidity: {humidity} %

☁ Weather: {weather}

🌬 Wind Speed: {wind_speed} m/s
"""
        )

    except Exception as e:
        result.config(text=f"Error: {e}")

# GUI Window
root = tk.Tk()
root.title("Weather Application")
root.geometry("500x450")
root.configure(bg="#87CEEB")

title = tk.Label(
    root,
    text="🌦 Weather Application",
    font=("Arial", 20, "bold"),
    bg="#87CEEB"
)
title.pack(pady=15)

city_entry = tk.Entry(root, width=30, font=("Arial", 14))
city_entry.pack(pady=10)

search_btn = tk.Button(
    root,
    text="Get Weather",
    command=get_weather,
    font=("Arial", 12)
)
search_btn.pack(pady=10)

result = tk.Label(
    root,
    text="Enter a city name",
    font=("Arial", 12),
    bg="#87CEEB",
    justify="left"
)
result.pack(pady=20)

root.mainloop()
