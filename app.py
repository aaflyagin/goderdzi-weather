@app.route("/weather")
def weather():
    url = "https://www.snow-forecast.com/resorts/Goderdzi/6day/mid"
    html = requests.get(url, headers={"User-Agent":"Mozilla/5.0"}).text

    import re, json

    match = re.search(r'var resortForecast = ({.*?});', html, re.S)

    if not match:
        return jsonify({"error":"forecast not found"})

    data = json.loads(match.group(1))

    temps = []
    snow = []

    for day in data["forecast"][:3]:
        temps.append(str(day["temp"]["mid"]) + "°C")
        snow.append(str(day["snow"]["mid"]) + " cm")

    return jsonify({
        "today_temp": temps[0],
        "tomorrow_temp": temps[1],
        "after_temp": temps[2],
        "today_snow": snow[0],
        "tomorrow_snow": snow[1],
        "after_snow": snow[2]
    })
