
#sudo apt-get install python-requests
#sudo pip install flask
#sudo pip install sensehat

from sense_hat import SenseHat
import time
from datetime import datetime
import requests
sense = SenseHat()
degree_symbol = u"\N{DEGREE SIGN}"

from sense_hat import SenseHat
import time
import requests # sudo apt-get install python-requests
sense = SenseHat()
degree_symbol = u"\N{DEGREE SIGN}"

from flask import Flask #sudo pip install flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/temperature")
def temperature():
    t = sense.get_temperature() * (9/5) + 32 # convert to degrees F
    t = str(round(t, 6)) # convert to string
    temperature_now = 'Temperature ' + t + degree_symbol + ' recorded at ' + time.strftime("%H:%M:%S:%f", time.localtime())
    return temperature_now

@app.route("/humidity")
def humidity():
    h = sense.get_humidity()
    h = str(round(h, 6))
    humidity_now = 'Humidity: ' + h + '% recorded at' + time.strftime("%H:%M:%S", time.localtime())
    return humidity_now

@app.route("/pressure")
def pressure():
    p = sense.get_pressure() / 33.864 # convert to inHg (inches of mercury)
    p = str(round(p, 6))
    pressure_now = 'Pressure ' + p + 'inHg recorded at ' + time.strftime("%H:%M:%S:%f", time.localtime())
    return pressure_now

@app.route("/snapshot")
def snapshot():
    sense.clear()
    t = sense.get_temperature() * (9/5) + 32 # convert to degrees F
    t = str(round(t, 5))                     # convert to string
    h = sense.get_humidity()
    h = str(round(h, 5))
    p = sense.get_pressure() / 33.864 # convert to inHg (inches of mercury)
    p = str(round(p, 5))
    o = sense.get_orientation()
    c = o["pitch"]
    c = str(round(c, 5))
    r = o["roll"]
    r = str(round(r, 5))
    w = o["yaw"]
    w = str(round(w, 5))
    a = sense.get_accelerometer_raw()
    x = a["x"]
    x = str(round(x,5))
    y = a["y"]
    y = str(round(y, 5))
    z = a["z"]
    z = str(round(z, 5))

    snap = [t,h,p,c,r,w,x,y,z]
    snapshot = "{" + "snapshot: " + str(datetime.now()) + ", " + str(snap) + "}"
    #snapshot = "{" + "snapshot: " + time.strftime("%H:%M:%S:%f", time.localtime()) + ", " + str(snap) + "}"
    return snapshot

    #print("{0},{1},{2},{3},{4},{5},{6},{7},{8} ".format(t, h, p, pitch, roll, yaw, x, y, z)

if __name__ == "__main__":
        app.run(host="0.0.0.0", port=80, debug=True)

#{
#  {"snapshot":
#    {
#     "timestamp":"datetime"
#     "readings":"[t,h,p,c,r,w,x,y,z]"
#    }
#  }
#
#{"snapshot":
#  {"timestamp":"datetime"
#   "readings":"[t,h,p,c,r,w,x,y,z]"}
#
#
#{}
#}

