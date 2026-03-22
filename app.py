from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    res = requests.get(url).json()
    return res.get("current_weather", None)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/weather", methods=["POST"])
def weather():
    lat = request.form.get("lat")
    lon = request.form.get("lon")

    if not lat or not lon:
        return "Location not provided"

    weather = get_weather(lat, lon)

    if not weather:
        return "Weather unavailable"

    return render_template(
        "result.html",
        temp=weather["temperature"],
        wind=weather["windspeed"]
    )

if __name__ == "__main__":
    app.run(debug=True)