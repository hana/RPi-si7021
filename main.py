import board
import adafruit_si7021

import datetime
import json
import sys, time

#from retry import retry

#@retry(tries=10, delay=1)
#def connect():
#    return i2c, sensor
    
    
try:
    #i2c, sensor = connect()
    
    sensor = adafruit_si7021.SI7021(board.I2C())
    time.sleep(1)
    JSON_Path = "./temp.json"

    if (len(sys.argv)-1) :
        JSON_Path = sys.argv[1]

    data = {
        "temperature": sensor.temperature,
        "humidity":sensor.relative_humidity,
        "update_at":str(datetime.datetime.now())
    }

    with open(JSON_Path, 'w') as f:
        json.dump(data, f, indent=4)
    
        print("Written to", JSON_Path)
    
except ValueError:
    print("Error occured. Maybe no sensor connected?")
