## Python Simple CLI API Client for OpenWeatherMap 

Simple CLI **python 3.7** to get current city temperature (Celcius) in Indonesia.
[OpenWeatherMap Api Doc](https://openweathermap.org/current "OpenWeatherMap Api Doc") | [Requirements](https://github.com/Freizello/Python-OpenWeatherApi-Client/blob/master/requirements.txt "Requirements")
### Screenshoot

![Screenshoot](https://user-images.githubusercontent.com/12061206/54583301-4fe3b500-4a46-11e9-8520-9b717795fc9a.gif)

### Usage
- Copy `.env.example` or create new file named `.env`  on root folder.
- Get your OpenWeatherMap API KEY from [here](https://home.openweathermap.org/ "here") (free for current city API)
- Copy your API KEY and Paste it to `.env` on `API_KEY='YOUR_OPENWHEATERAPI_API_KEY'`

### Full Response from OpenWeatherMap API
Here a full response result from OpenWeatherMap API just in case you want to get another information like Longitude, Latitude, current weather, etc.
```json
{
    "coord": {
        "lon": 98.67,
        "lat": 3.59
    },
    "weather": [
        {
            "id": 721,
            "main": "Haze",
            "description": "haze",
            "icon": "50d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 30,
        "pressure": 1012,
        "humidity": 70,
        "temp_min": 30,
        "temp_max": 30
    },
    "visibility": 5000,
    "wind": {
        "speed": 3.1,
        "deg": 90
    },
    "clouds": {
        "all": 40
    },
    "dt": 1552964400,
    "sys": {
        "type": 1,
        "id": 9412,
        "message": 0.0063,
        "country": "ID",
        "sunrise": 1552951810,
        "sunset": 1552995386
    },
    "id": 1214520,
    "name": "Medan",
    "cod": 200
}
```

### License
[MIT License](https://opensource.org/licenses/MIT "MIT License ")