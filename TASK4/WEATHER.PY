import tkinter as tk
import requests
import json

# Replace with your own API key obtained from OpenWeatherMap
API_KEY = "d43069d9615e4bd48c1124057240203"

def get_weather():
    city = city_entry.get()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        weather_description.config(text=f"Description: {data['weather'][0]['description']}")
        temperature.config(text=f"Temperature: {data['main']['temp']:.2f} °C")
        feels_like.config(text=f"Feels Like: {data['main']['feels_like']:.2f} °C")
    else:
        weather_description.config(text="Error: Could not fetch weather data")
        temperature.config(text="")
        feels_like.config(text="")

# Create the main window
root = tk.Tk()
root.title("Weather App")  # Adjust the title as desired

# City entry label and field
city_label = tk.Label(root, text="Enter City:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

# Get weather button
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

# Weather information labels
weather_description = tk.Label(root, text="")
weather_description.pack()

temperature = tk.Label(root, text="")
temperature.pack()

feels_like = tk.Label(root, text="")
feels_like.pack()

root.mainloop()
