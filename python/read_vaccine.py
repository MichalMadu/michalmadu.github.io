import json
import requests
response = requests.get("https://onemocneni-aktualne.mzcr.cz/api/v1/covid-19/pomucky.json")
overview = json.loads(response.text)

#print(overview['modified'])

data = overview["data"][10].items()

print(data)