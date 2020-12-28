#!/bin/bash

cd `dirname $0`;
source .venv/bin/activate;
python main.py /home/pi/www/data/room.json;
