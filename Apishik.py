import requests
import os
from typing import Dict, Any, Optional
from flask import Flask, request, jsonify

app = Flask(__name__)

WEATHER_API_KEY = "0bb8bdd78f1648de39abcb3a9ce777bd"  
WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"

def getWeather(city: str) -> Optional[Dict[str, Any]]:
    
    
    try:
        
        params = {
            "q": city,
            "appid": WEATHER_API_KEY,
            "units": "metric",  
            "lang": "ru"  
        }
        
        
        response = requests.get(
            WEATHER_API_URL, 
            params=params, 
            timeout=5
        )
        
        
        if response.status_code == 401:
            return {"error": "Неверный API ключ (401)"}
        elif response.status_code == 404:
            return {"error": f"Город '{city}' не найден (404)"}
        elif response.status_code != 200:
            return {"error": f"Ошибка API: {response.status_code}"}
        
        
        data = response.json()
        
        
        result = {
            "Город": data["name"],
            "Температура": f"{data['main']['temp']:.1f}°C",
            "Описание": data["weather"][0]["description"].capitalize(),
            "Влажность": f"{data['main']['humidity']}%",
            "Скорость ветра": f"{data['wind']['speed']:.1f} м/с"
        }
        
        return result
        
    except requests.Timeout:
        return {"error": "Прошло слишком много с начала запроса"}
    except requests.ConnectionError:
        return {"error": "Ошибка подключения "}
    except Exception as e:
        return {"error": f"Ошибка: {str(e)}"}


@app.route("/weather", methods=["GET"])
def weatherEndpoint():
    
    city = request.args.get("city")
    
    
    if not city:
        return jsonify({
            "error": "Нужно ввести город в ссылке",
            "example": "/weather?city=Moscow"
        }), 400
    
    
    weather_data = getWeather(city)
    
    if "error" in weather_data:
        error_msg = weather_data["error"]
        
        
        if "401" in error_msg:
            return jsonify(weather_data), 401
        elif "404" in error_msg:
            return jsonify(weather_data), 404
        elif "Timeout" in error_msg:
            return jsonify(weather_data), 504
        else:
            return jsonify(weather_data), 500
    
    
    return jsonify(weather_data), 200


if __name__ == "__main__":
    print("Пример запроса: http://localhost:5000/weather?city=Moscow")
    app.run(debug=True, port=5000)