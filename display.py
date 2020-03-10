import requests
import json
import time
import math
 
import Adafruit_CharLCD as LCD

url = "https://coronavirus-tracker-api.herokuapp.com/all"
id = 85 # country ID

# Raspberry Pi configuration:
lcd_rs = 27  # Change this to pin 21 on older revision Raspberry Pi's
lcd_en = 22
lcd_d4 = 25
lcd_d5 = 24
lcd_d6 = 23
lcd_d7 = 18
lcd_red   = 4
lcd_green = 17
lcd_blue  = 7  # Pin 7 is CE1
# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_RGBCharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                              lcd_columns, lcd_rows, lcd_red, lcd_green, lcd_blue)

while True:
    response = requests.get(url)
    data = response.text

    parsed = json.loads(data)

    confirmed_w = repr(parsed.get("latest").get("confirmed"))
    deaths_w = repr(parsed.get("latest").get("deaths"))
    recovered_w = repr (parsed.get("latest").get("recovered"))


    confirmed_ch = repr(parsed.get("confirmed").get("locations")[id].get("latest"))
    deaths_ch = repr(parsed.get("deaths").get("locations")[id].get("latest"))
    recovered_ch = repr(parsed.get("recovered").get("locations")[id].get("latest"))


    
    lcd.set_color(0.8, 0.5, 0.0)
    lcd.clear()
    lcd.message('Swiss Cases ' + confirmed_ch)
    lcd.message('\nWW Cases ' + confirmed_w)

    time.sleep(15.0)

    lcd.set_color(0.0, 1.0, 0.0)
    lcd.clear()
    lcd.message('CH Recoverd ' + recovered_ch)
    lcd.message('\nWW ' + recovered_w)

    time.sleep(15.0)

    lcd.set_color(1.0, 0.0, 0.0)
    lcd.clear()
    lcd.message('CH Dead ' + deaths_ch)
    lcd.message('\nWW Dead ' + deaths_w)

    time.sleep(15.0)


