#!/bin/bash

pip install requests
sudo apt-get install build-essential python-dev python-smbus python-pip git
sudo pip install RPi.GPIO

cd ~
git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git
cd Adafruit_Python_CharLCD
sudo python setup.py install