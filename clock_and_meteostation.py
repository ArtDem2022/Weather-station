appid = "OpenWeather ApiKey"

import requests
from tkinter import *  
import datetime

def get_wind_direction(deg): 
    l = ['С ','СВ',' В','ЮВ','Ю ','ЮЗ',' З','СЗ']
    for i in range(0,8):
        step = 45.
        min = i*step - 45/2.
        max = i*step + 45/2.
        if i == 0 and deg > 360-45/2.:
            deg = deg - 360
        if deg >= min and deg <= max:
            res = l[i]
            break
    return res

city_id = 496035 

window = Tk()  
window.title("Weather")  

def update():
    now = datetime.datetime.now()
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
            params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    nowtime.config(text=str(now.hour)+":"+str(now.minute),font=("Arial", 50))
    desc.config( text=("Погода в "+ data['name'] + ": "+ data['weather'][0]['description']),font=("Arial", 25))

    temp.config( text=("Температура: " + str(int(data['main']['temp'])) + " ℃"),font=("Arial", 25))

    feelsLike.config( text=("Ощущается как: "+ str(int(data['main']['feels_like'])) + " ℃"),font=("Arial", 25))

    pressure.config( text=("Давление: "+ str(float(data['main']['pressure'])*0.75) + " мм"),font=("Arial", 25))

    humidity.config( text=("Влажность: "+ str(data['main']['humidity'])+"%"),font=("Arial", 25))

    wind.config(text=("Ветер: " + str(data['wind']['speed'])+" м/с." + get_wind_direction(data['wind']['deg'])),font=("Arial", 25))

    window.after(1000, update)

nowtime=Label()
nowtime.pack(side=TOP)
desc = Label()
desc.pack(side=TOP)
temp = Label()
temp.pack(side=TOP)
feelsLike = Label()
feelsLike.pack(side=TOP)
pressure = Label()
pressure.pack(side=TOP)
humidity = Label()
humidity.pack(side=TOP)
wind = Label()
wind.pack(side=TOP)

window.after(1000, update)
window.mainloop()
