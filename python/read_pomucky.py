import json
import requests
response = requests.get("https://onemocneni-aktualne.mzcr.cz/api/v1/covid-19/pomucky.json")
overview = json.loads(response.text)

#print(overview['data'])

#jsonlist = overview['data']['kraj'][10]
#print(jsonlist)

pocetpomucek = overview['data']

#for item in spaces:
#    if item.get('use') == "examination" :
#       item['price'] = 175

#print(datastore["office"]["medical"][2])

for item in pocetpomucek:
    if item.get('pomucka') == "Roušky" :
        pocet = item.get('pocet')
        kraj = item.get('kraj')
        print(kraj+" : "+str(pocet))

#for item in pocetpomucek:
#    if item.get('pomucka') == "Roušky" :
#        celkem = sum(int(pocet])
#print("Celkem: "+str(celkem))