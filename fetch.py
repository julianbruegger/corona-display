import requests
import json
import time
from datetime import date
url = "https://coronavirus-tracker-api.herokuapp.com/all"
id = 85 # country ID

response = requests.get(url)
data = response.text

parsed = json.loads(data)

confirmed_w = repr(parsed.get("latest").get("confirmed"))
deaths_w = repr(parsed.get("latest").get("deaths"))
recovered_w = repr (parsed.get("latest").get("recovered"))

country_code = repr(parsed.get("confirmed").get("locations")[id].get("country_code"))
country_code_filter = country_code[1:3]
confirmed_c = repr(parsed.get("confirmed").get("locations")[id].get("latest"))
deaths_c = repr(parsed.get("deaths").get("locations")[id].get("latest"))
recovered_c = repr(parsed.get("recovered").get("locations")[id].get("latest"))

float_w = float(confirmed_w)
float_c = float(confirmed_c)
population_world = float("8000000000")
population_country = float("8000000")
percent_w = '{:.7f}'.format(float_w / population_world)
percent_c = '{:.7f}'.format(float_c / population_country)

print (percent_w)
print (percent_c)

print ("Confirmed WW " + confirmed_w)
print ("deaths WW " + deaths_w)
print ("recovered WW " + recovered_w)

print ("Confirmed " + country_code_filter +" "+ confirmed_c)
print ("deaths "+ country_code_filter +" " + deaths_c)
print ("recovered  " + country_code_filter +" "+ recovered_c)