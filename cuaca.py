# https://api.openweathermap.org/data/2.5/weather?q=Medan&appid=f24242b8e5df44581321fec030a7126a



import requests

apiKey = 'f24242b8e5df44581321fec030a7126a'
kota = input('Masukkan nama kota di Indonesia : ')

resDoc = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+kota+',id&units=metric&appid='+apiKey).json()

def getTemperature(kota, apiKey):
    res = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+kota+',id&units=metric&appid='+apiKey).json()
    
    return res['main']

if __name__ == '__main__' :
    
    print(getTemperature(kota, apiKey))
