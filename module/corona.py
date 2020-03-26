from bs4 import BeautifulSoup
import requests
import csv
import sys
import time
from config import *



page_c = requests.get(url_c)
soup_c = BeautifulSoup(page_c.text, 'html.parser')
page_w = requests.get(url_w)
soup_w = BeautifulSoup(page_w.text, 'html.parser')

#print (soup_c)ython

country = soup_c.select('h2')[0].text.strip()
infections_c = soup_c.select('h2')[1].text.strip()
deaths_c = soup_c.select('h2')[2].text.strip()
survived_c = soup_c.select('h2')[3].text.strip()
today_c = soup_c.select('h2')[4].text.strip()

first, last = country.split()
    
infections_w = soup_w.select('h2')[1].text.strip()
deaths_w = soup_w.select('h2')[2].text.strip()
survived_w = soup_w.select('h2')[3].text.strip()
today_w = soup_w.select('h2')[4].text.strip()

percent_c = str('{:.7f}'.format(int(infections_c.replace(',','')) / int(population_c))+(" %"))
percent_w = str('{:.7f}'.format(int(infections_w.replace(',','')) / int(population_w))+(" %"))

