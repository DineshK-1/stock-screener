import requests
import json

url = "https://coinranking1.p.rapidapi.com/coins"

querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"24h","tiers":"1","orderBy":"marketCap","orderDirection":"desc","limit":"50","offset":"0"}

headers = {
    'x-rapidapi-host': "coinranking1.p.rapidapi.com",
    'x-rapidapi-key': "1308a3e81fmshc5c7805a1477572p1ac776jsn696bc69cace6"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

with open("Coins.json", "w") as f:
    json.dump(response.json(), f)
