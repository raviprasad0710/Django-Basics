import requests


url = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
mydata=url.json

print(type(mydata))
print(mydata["bpi"]["USD"]["rate"])
print(mydata.keys())
