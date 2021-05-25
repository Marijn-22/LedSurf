#!/bin/sh
# launcher.sh
# automatically start script

cd /
source home/pi/led_strip/LED_env/bin/activate
cd home/pi/led_strip/LedSurf/ledstrip
sudo python functions.py -c