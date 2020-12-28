# RPi-si7021
- Python3
- Raspberry Pi
- May need to apply [I2C Clock Stretching](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/i2c-clock-stretching)

## Usage
1. Install requirements.
2. Run main.py
3. Check the output written in `temp.json`

Specifying the path as the second command-line argument changes the output location.  
ex) `python3 main.py /path/to/your/output.json`