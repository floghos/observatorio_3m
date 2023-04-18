import requests 
import json

# x = requests.get('https://w3schools.com/python/demopage.htm')

source = "moon"
req = requests.get(f'http://localhost:8090/api/objects/info?name={source}&format=json')
data = req.json()
print(f'Altitude: {data["altitude"]}\nAzimuth: {data["azimuth"]}')

