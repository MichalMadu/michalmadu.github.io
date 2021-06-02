import urllib
import json
mysumcnt = 0
input = urllib.urlopen('https://onemocneni-aktualne.mzcr.cz/api/v1/covid-19/pomucky.json').read()

info = json.loads(input)
myinfo = info['comments']

for item in myinfo:
    mycnt = item['count']
    mysumcnt += mycnt
print(mysumcnt)