import requests
import json
import time
from datetime import date
url = "https://coronavirus-tracker-api.herokuapp.com/all"
url_ov = "http://transport.opendata.ch/v1/stationboard?station=lucerne&limit=1"

id = 85 # country ID
# Enter own numbers for your coubtry
population_world = float("8000000000")
population_country = float("8570000")
# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16

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

message = category + number +' to ' + destination + '\nExp: ' + departure_time 
lenght = len(message)

print (lenght - lcd_columns)
print (message)

print (percent_w)
print (percent_c)


print ("Confirmed WW " + confirmed_w)
print ("deaths WW " + deaths_w)
print ("recovered WW " + recovered_w)

print ("Confirmed " + country_code_filter +" "+ confirmed_c)
print ("deaths "+ country_code_filter +" " + deaths_c)
print ("recovered  " + country_code_filter +" "+ recovered_c)