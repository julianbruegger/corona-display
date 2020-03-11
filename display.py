from bs4 import BeautifulSoup
import Adafruit_CharLCD as LCD
import requests
import time
import math

# Insert your URL here
url_c = "https://corona.help/country/switzerland"
# Insert your Population here
population_c = "8570000"
cc = "CH"
population_w = "7770173166"
url_w ="https://corona.help/"


Raspberry Pi configuration:
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

    page_c = requests.get(url_c)
    soup_c = BeautifulSoup(page_c.text, 'html.parser')
    page_w = requests.get(url_w)
    soup_w = BeautifulSoup(page_w.text, 'html.parser')

    # print (soup)
    infections_c = soup_c.select('h1')[1].text.strip()
    deaths_c = soup_c.select('h1')[2].text.strip()
    survived_c = soup_c.select('h1')[3].text.strip()

    infections_w = soup_w.select('h1')[1].text.strip()
    deaths_w = soup_w.select('h1')[2].text.strip()
    survived_w = soup_w.select('h1')[3].text.strip()
    percent_c = '{:.7f}'.format(int(infections_c) / int(population_c))
    percent_w = '{:.7f}'.format(int(infections_w) / int(population_w))


    lcd.set_color(1.0, 0.54, 0.0)
    lcd.clear()
    lcd.message(cc + ' Cases ' + confirmed_c)
    lcd.message('\nWW Cases ' + confirmed_w)

    time.sleep(20.0)

    lcd.set_color(0.0, 1.0, 0.0)
    lcd.clear()
    lcd.message(cc + ' Recoverd ' + recovered_c)
    lcd.message('\nWW ' + recovered_w)

    time.sleep(20.0)

    lcd.set_color(1.0, 0.0, 0.0)
    lcd.clear()
    lcd.message(cc +' Dead ' + deaths_c)
    lcd.message('\nWW Dead ' + deaths_w)

    time.sleep(20.0)

    lcd.set_color(0.2, 0.5, 0.4)
    lcd.clear()
    lcd.message('% of Swiss Population')
    lcd.message('\n' + percent_w + '%')
    
    time.sleep(20.0)