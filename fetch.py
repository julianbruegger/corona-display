from bs4 import BeautifulSoup
import requests

# Insert your URL here
url_c = "https://corona.help/country/switzerland"
# Insert your Population here
population_c = "8570000"
population_w = "7770173166"
url_w ="https://corona.help/"

page_c = requests.get(url_c)
soup_c = BeautifulSoup(page_c.text, 'html.parser')
page_w = requests.get(url_w)
soup_w = BeautifulSoup(page_w.text, 'html.parser')

# print (soup)
country = soup_c.select('h1')[0].text.strip()
infections_c = soup_c.select('h1')[1].text.strip()
deaths_c = soup_c.select('h1')[2].text.strip()
survived_c = soup_c.select('h1')[3].text.strip()

first, *middle, last = country.split()

infections_w = soup_w.select('h1')[1].text.strip()
deaths_w = soup_w.select('h1')[2].text.strip()
survived_w = soup_w.select('h1')[3].text.strip()
percent_c = str('{:.7f}'.format(int(infections_c) / int(population_c))+(" %"))
percent_w = str('{:.7f}'.format(int(infections_w) / int(population_w))+(" %"))


print("Cases in " +(last))
print(("Infections: ") + infections_c + (", Deaths: ") + deaths_c+(", Survived: ")+survived_c)
print("Numbers Worldwide")
print(("Infections: ")+infections_w+(", Deaths: ")+ deaths_w +(", Survivied: ") +survived_w)

print (percent_c + (" of ")+(last)+ (" citicens are infected!"))
print (percent_w + (" of world citicens are infected!"))
print ()


