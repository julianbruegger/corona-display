from bs4 import BeautifulSoup
import requests
import csv
import sys
import time


# Insert your country URL here
url_b = "https://corona.help/country/united-states"
url_c = "https://corona.help/country/switzerland"

# Insert your country Population here
population_c = "8173166"
population_w = "7770173166" # World-population
url_w ="https://corona.help/"
# Your Country-Code
cc = "CH"

page_b = requests.get(url_b)
soup_b = BeautifulSoup(page_b.text, 'html.parser')
page_c = requests.get(url_c)
soup_c = BeautifulSoup(page_c.text, 'html.parser')
page_w = requests.get(url_w)
soup_w = BeautifulSoup(page_w.text, 'html.parser')

#print (soup_c)ython

country_b = soup_b.select('h2')[0].text.strip()
infections_b = soup_b.select('h2')[1].text.strip()
deaths_b = soup_b.select('h2')[3].text.strip()
survived_b = soup_b.select('h2')[5].text.strip()
today_b = soup_b.select('h2')[2].text.strip()

first_b = country_b.rsplit(' ',1)[0]

country_c = soup_c.select('h2')[0].text.strip()
infections_c = soup_c.select('h2')[1].text.strip()
deaths_c = soup_c.select('h2')[3].text.strip()
survived_c = soup_c.select('h2')[5].text.strip()
today_c = soup_c.select('h2')[2].text.strip()

first_c = country_c.rsplit(' ',1)[0]
    
infections_w = soup_w.select('h2')[1].text.strip()
deaths_w = soup_w.select('h2')[3].text.strip()
survived_w = soup_w.select('h2')[5].text.strip()
today_w = soup_w.select('h2')[2].text.strip()

percent_c = str('{:.7f}'.format(int(infections_c.replace(',','')) / int(population_c))+(" %"))
percent_w = str('{:.7f}'.format(int(infections_w.replace(',','')) / int(population_w))+(" %"))

