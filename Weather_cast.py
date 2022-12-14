import tkinter as tk
import time
import requests


def getweather(canvas):
    city = textField.get()
    api_key = 'b09b579f44c76f6b427d548fdcfccdfe'
    url = 'https://api.openweathermap.org/data/2.5/weather?appid=' + api_key + '&q=' + city

    response = requests.get(url).json()

    condition = response['weather'][0]['main']
    temp = int(response['main']['temp']) - 273.15
    min_temp = int(response['main']['temp_min']) - 273.15
    max_temp = int(response['main']['temp_max']) - 273.15
    pressure = response['main']['pressure']
    # wilgotność
    humidity = response['main']['humidity']
    wind = response['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(response['sys']['sunrise'] - (response['timezone'])))
    sunset = time.strftime('%I:%M:%S', time.gmtime(response['sys']['sunset'] - (response['timezone'])))

    weather = f"{condition} {temp:.2f}°C\n"
    data = f"Max Temp: {max_temp:.2f}°C\n" \
           f"Min Temp: {min_temp:.2f}°C\n" \
           f"Pressure: {pressure}\n" \
           f"Humidity: {humidity}\n" \
           f"Wind: {wind}\n" \
           f"Humidity: {humidity}\n" \
           f"Sunrise: {sunrise}\n" \
           f"Sunset: {sunset}"
    label1.config(text=weather)
    label2.config(text=data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getweather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop()
