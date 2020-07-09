import urllib.request
import json
import os
number=input("pls write ip adress : ")
url="https://ipinfo.io/"+number+"/json"
try: 
    number=urllib.request.urlopen(url)
except:
    print("ip not found")
listApi=json.load(number)
print(listApi)
