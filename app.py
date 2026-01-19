from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Goderdzi weather API is working"

@app.route("/weather")
def weather():
    url = "https://www.snow-forecast.com/resorts/Goderdzi/6day/mid"
    html = requests.get(url, headers={"User-Agent":"Mozilla/5.0"}).text
    soup = BeautifulSoup(html, "html.parser")

    temps = [x.text for x in soup.select(".forecast-table-temp span")]
    snow = [x.text for x in soup.select(".forecast-table-snow span")]

    return jsonify({
        "today_temp": temps[0] if len(temps)>0 else "",
        "tomorrow_temp": temps[1] if len(temps)>1 else "",
        "after_temp": temps[2] if len(temps)>2 else "",
        "today_snow": snow[0] if len(snow)>0 else "",
        "tomorrow_snow": snow[1] if len(snow)>1 else "",
        "after_snow": snow[2] if len(snow)>2 else ""
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
