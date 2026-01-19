from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Goderdzi weather API is working"

@app.route("/weather")
def weather():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=41.635503"
        "&longitude=42.491022"
        "&daily=temperature_2m_max,temperature_2m_min,snowfall_sum"
        "&timezone=auto"
    )

    data = requests.get(url).json()
    days = data["daily"]

    return jsonify({
        "today_temp": f'{days["temperature_2m_min"][0]}°C / {days["temperature_2m_max"][0]}°C',
        "today_snow": f'{days["snowfall_sum"][0]} cm',

        "tomorrow_temp": f'{days["temperature_2m_min"][1]}°C / {days["temperature_2m_max"][1]}°C',
        "tomorrow_snow": f'{days["snowfall_sum"][1]} cm',

        "after_temp": f'{days["temperature_2m_min"][2]}°C / {days["temperature_2m_max"][2]}°C',
        "after_snow": f'{days["snowfall_sum"][2]} cm'
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
