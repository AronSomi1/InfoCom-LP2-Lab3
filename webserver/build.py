from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import time
import redis

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = "dljsaklqk24e21cjn!Ew@@dsa5"
socket = SocketIO(app, cors_allowed_origins="*")

# change this so rhat you can connect to your own redis server
# ===============================================
redis_server = redis.Redis(host="localhost", port="7777")
# ===============================================


# Translate OSM coordinate (longitude, latitude) to SVG coordinates (x,y).
# Input coords_osm is a tuple (longitude, latitude).
def translate(coords_osm):
    x_osm_lim = (13.143390664, 13.257501336)
    y_osm_lim = (55.678138854000004, 55.734680845999996)

    x_svg_lim = (0, 473)
    y_svg_lim = (0, 397)

    x_osm = coords_osm[0]
    y_osm = coords_osm[1]

    x_ratio = (x_svg_lim[1] - x_svg_lim[0]) / (x_osm_lim[1] - x_osm_lim[0])
    y_ratio = (y_svg_lim[1] - y_svg_lim[0]) / (y_osm_lim[1] - y_osm_lim[0])
    x_svg = x_ratio * (x_osm - x_osm_lim[0]) + x_svg_lim[0]
    y_svg = y_ratio * (y_osm_lim[1] - y_osm) + y_svg_lim[0]

    return x_svg, y_svg


def MinutesAndSeconds(time_data):  # fix this !!
    input = int(time_data)
    mm, ss = divmod(input, 60)
    return mm, ss


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/map.html/", methods=["GET"])
def map():
    return render_template("map.html")


@app.route("/beställning.html/")
def beställning():
    return render_template("beställning.html")


@socket.on("get_location")
def get_location():
    while True:
        longitude = float(redis_server.get("longitude"))
        latitude = float(redis_server.get("latitude"))
        minutes, seconds = MinutesAndSeconds(float(redis_server.get("time_left")))
        x_svg, y_svg = translate((longitude, latitude))
        emit("get_location", (x_svg, y_svg, minutes, seconds))
        time.sleep(0.1)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
