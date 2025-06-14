import requests
from datetime import datetime

API_KEY = "a641892d56a4a927c1e0628d3305b09b"


def get_real_temp(city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['main']['temp']
    else:
        print("Real API Error:", response.json())
        return None

def get_predicted_temp(city_name, day, month, hour):
    url = "http://127.0.0.1:5000/predict"
    payload = {
        "city_name": city_name,
        "DayofYear": day,
        "month": month,
        "Hour": hour
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()['predicted_temp']
    else:
        print("Your API Error:", response.json())
        return None


def compare(city):
    now = datetime.now()
    day = now.timetuple().tm_yday
    month = now.month
    hour = now.hour

    real = get_real_temp(city)
    predicted = get_predicted_temp(city, day, month, hour)
    
    difference = round(abs(real - predicted))

   
    print(f" Predicted Temp: {predicted} °C")
    print(f" Real Temp from OpenWeather: {real} °C")
    print(f"difference between actual and predicted temp is:{difference} °C")
    
compare("Ahmedabad")
compare("Mumbai")
