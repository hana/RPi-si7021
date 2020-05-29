import adafruit_si7021

from busio import I2C
from board import SCL, SDA

from metro import Metro


import json

i2c = I2C(SCL, SDA)
sensor = adafruit_si7021.SI7021(i2c)

JSON_Path = "./temp.json"


try:
    data = {
        "temperature": sensor.temperature,
        "humidity":sensor.relative_humidity
    }

    with open(JSON_Path, 'w') as f:
        json.dump(data, f, indent=4)

except OSError:
    print("Error occured. Maybe no sensor connected?")
