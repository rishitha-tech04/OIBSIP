import requests

print("Weather App")

API_KEY = "47cf7b3f1548602346b39fd92037bd5a"

city = input("Enter city name: ").strip()

if city == "":
    print("City name cannot be empty.")
else:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            print("\nWeather Report")
            print("City:", data["name"])
            print("Country:", data["sys"]["country"])
            print("Temperature:", data["main"]["temp"], "°C")
            print("Feels Like:", data["main"]["feels_like"], "°C")
            print("Humidity:", data["main"]["humidity"], "%")
            print("Weather:", data["weather"][0]["description"].title())
            print("Wind Speed:", data["wind"]["speed"], "m/s")
        else:
            print("City not found or Invalid API Key.")

    except requests.exceptions.RequestException:
        print("Unable to connect. Please check your internet connection.")