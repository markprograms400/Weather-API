import requests

api_key = "9ae16217c7a6afde32572233bcb87e90"

city = input("Enter a city: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
print("Status Code:", response.status_code)
print("Response JSON:")
data = response.json()

temp = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
condition = data["weather"][0]["description"]
city = data["name"]

print(f"Weather in {city}:")
print(f"Temperature: {temp}°C (feels like {feels_like}°C)")
print(f"Condition: {condition.capitalize()}")