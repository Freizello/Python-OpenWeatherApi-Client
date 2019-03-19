# https://api.openweathermap.org/data/2.5/weather?q=Medan&appid=f24242b8e5df44581321fec030a7126a

import os, requests
import config

apiKey = os.getenv('API_KEY')
kota = input('Masukkan nama kota di Indonesia : ')

def getTemperature(kota, apiKey):
    res = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+kota+',id&units=metric&appid='+apiKey).json()
    
    return res['main']

if __name__ == '__main__' :
    if apiKey : 
        print(getTemperature(kota, apiKey))
    else :
        print('ERROR : API KEY OpenWeatherApi kosong')
        