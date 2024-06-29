#Kimiya Karami
import requests
import xmltodict
import json

url = "https://sahmeto.com/crypto-sitemap.xml"
response = requests.get(url)
data = xmltodict.parse(response.content)

json_data = json.dumps(data, indent=4)
print(json_data)
