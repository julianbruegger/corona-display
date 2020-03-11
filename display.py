from bs4 import BeautifulSoup
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