import requests
import json

url = "https://coronavirus-tracker-api.herokuapp.com/all"
response = requests.get(url)
data = response.text

parsed = json.loads(data)
latest = parsed["latest"]
confirmed = parsed["confirmed"]

confirmed_w = (latest.get("confirmed"))
deaths_w = (latest.get("deaths"))
recovered_w = (latest.get("recovered"))
confirmed_s = (confirmed.get("locations")[87].get("latest"))

print (confirmed_w)
print (confirmed_s)
