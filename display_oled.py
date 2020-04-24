import time
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
from bs4 import BeautifulSoup
import requests
import sys
import math


#This is the following code from the Adafruit Learn Page for the ssd1306 display. I will leave the original code and comments here!

# Create the I2C interface.

i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!

disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Clear display.

disp.fill(0)
disp.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.

width = disp.width
height = disp.height
image = Image.new("1", (width, height))

# Get drawing object to draw on image.

draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.

draw.rectangle((0, 0, width, height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.

padding = -2
top = padding
bottom = height - padding

# Move left to right keeping track of the current x position for drawing shapes.

x = 0

# Load default font.

font = ImageFont.load_default()

#Here is the updated code from the original LCD display, updated for use with the OLED display
while True:
    from module.corona import *
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    #These will take the data from the original file and place them as text on the display.
    draw.text((x, top + 0), "COVID-19 INFECTIONS", font=font, fill=255)
    draw.text((x, top + 8), (cc) + (" infected ") + (infections_c), font=font, fill=255)
    draw.text((x, top + 16), "WW Infected " + (infections_w), font=font, fill=255)
    # Display image. This command pushes the image to the display, and will wait 10 seconds
    disp.image(image)
    disp.show()
    time.sleep(10)


    #The same code as before, but this one is displaying death information
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((x, top + 0), "COVID-19 DEATHS", font=font, fill=255)
    draw.text((x, top + 8), (cc) + (" Deaths ") + (deaths_c), font=font, fill=255)
    draw.text((x, top + 16), "WW Deaths " + (deaths_w), font=font, fill=255)
    disp.image(image)
    disp.show()
    time.sleep(10)
    
    #Displays Recoveries
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((x, top + 0), "COVID-19 Recoveries", font=font, fill=255)
    draw.text((x, top + 8), (cc) + (" Recoveries ") + (survived_c), font=font, fill=255)
    draw.text((x, top + 16), "WW Recoveries " + (survived_w), font=font, fill=255)
    disp.image(image)
    disp.show()
    time.sleep(10)

    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((x, top + 0), "COVID-19 Tracker", font=font, fill=255)
    draw.text((x, top + 8), "Created by:", font=font, fill=255)
    draw.text((x, top + 16), "Julian Bruegger", font=font, fill=255)
    draw.text((x, top + 24), "Adapted for OLED by:", font=font, fill=255)
    draw.text((x, top + 32), "Harrison Thow", font=font, fill=255)
    disp.image(image)
    disp.show()
    time.sleep(10)
    

