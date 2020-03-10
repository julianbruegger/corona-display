import requests
import json
import time
import math
 
import Adafruit_CharLCD as LCD

url = "https://coronavirus-tracker-api.herokuapp.com/all"
url_ov = "http://transport.opendata.ch/v1/stationboard?station=lucerne&limit=1"

id = 85 # country ID

population_world = float("8000000000")
population_country = float("8570000")

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

    response_ov = requests.get(url_ov)
    data_ov = response_ov.text

    parsed_ov = json.loads(data_ov)


    station = (parsed_ov.get("station").get("name"))
    destination = (parsed_ov.get("stationboard")[0].get("to"))
    delay = (parsed_ov.get("stationboard")[0].get("stop").get("delay"))
    name = (parsed_ov.get("stationboard")[0].get("name"))
    number = (parsed_ov.get("stationboard")[0].get("number"))
    category = (parsed_ov.get("stationboard")[0].get("category"))
    departure = parsed_ov.get("stationboard")[0].get("stop").get("departure")

    departure_time = departure[-13:16]
    departure_delay = departure[-4:22]



    confirmed_w = repr(parsed.get("latest").get("confirmed"))
    deaths_w = repr(parsed.get("latest").get("deaths"))
    recovered_w = repr (parsed.get("latest").get("recovered"))

    country_code = repr(parsed.get("confirmed").get("locations")[id].get("country_code"))
    cc_formated = country_code[2:4]
    confirmed_c = repr(parsed.get("confirmed").get("locations")[id].get("latest"))
    deaths_c = repr(parsed.get("deaths").get("locations")[id].get("latest"))
    recovered_c = repr(parsed.get("recovered").get("locations")[id].get("latest"))

    float_w = float(confirmed_w)
    float_c = float(confirmed_c)
    percent_w = '{:.7f}'.format(float_w / population_world)
    percent_c = '{:.7f}'.format(float_c / population_country)

    wait = 0.9
    message = category + number +' to ' + destination + '\nExp: ' + departure_time 
    lcd.set_color(0.1, 0.1, 0.1)
    lcd.clear()
    lcd.message(message)

    for i in range (10):
        time.sleep(wait)
        lcd.move_left()

    for i in range (10):
        time.sleep(wait)
        lcd.move_right()
         
    time.sleep(20.0)

    lcd.set_color(1.0, 0.54, 0.0)
    lcd.clear()
    lcd.message(cc_formated + ' Cases ' + confirmed_c)
    lcd.message('\nWW Cases ' + confirmed_w)

    time.sleep(20.0)

    lcd.set_color(0.0, 1.0, 0.0)
    lcd.clear()
    lcd.message(cc_formated + ' Recoverd ' + recovered_c)
    lcd.message('\nWW ' + recovered_w)

    time.sleep(20.0)

    lcd.set_color(1.0, 0.0, 0.0)
    lcd.clear()
    lcd.message(cc_formated +' Dead ' + deaths_c)
    lcd.message('\nWW Dead ' + deaths_w)

    time.sleep(20.0)

    lcd.set_color(0.2, 0.5, 0.4)
    lcd.clear()
    lcd.message('% of Swiss Population')
    lcd.message('\n' + percent_w + '%')
    
    time.sleep(20.0)

    


