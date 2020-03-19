from bs4 import BeautifulSoup
import requests
import csv
import sys
import time

# Insert your URL here
url_c = "https://corona.help/country/switzerland"
# Insert your Population here
population_c = "8173166"
population_w = "7770173166"
url_w ="https://corona.help/"

page_c = requests.get(url_c)
soup_c = BeautifulSoup(page_c.text, 'html.parser')
page_w = requests.get(url_w)
soup_w = BeautifulSoup(page_w.text, 'html.parser')

#print (soup_c)

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

    
print("Cases in " +(first))
print(("Infections: ") + infections_c + (", Deaths: ") + deaths_c+(", Survived: ")+survived_c)
print("Numbers Worldwide")
print(("Infections: ")+infections_w+(", Deaths: ")+ deaths_w +(", Survived: ") +survived_w)

<<<<<<< HEAD
print (percent_c + (" of ")+(first)+ (" citicens are infected!"))
print (percent_w + (" of world citicens are infected!"))
#print ()
=======
print (percent_c + (" of ")+(last)+ (" citizens are infected!"))
print (percent_w + (" of world citizens are infected!"))
print ()
>>>>>>> b055c788972f0ba38dd50727d9e75908a0579037


