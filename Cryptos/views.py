from django.shortcuts import render
import requests
import json

def IndexCrypto(request):
    url = "https://coinranking1.p.rapidapi.com/coins"

    querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"24h","tiers":"1","orderBy":"marketCap","orderDirection":"desc","limit":"50","offset":"0"}

    headers = {
    'x-rapidapi-host': "coinranking1.p.rapidapi.com",
    'x-rapidapi-key': "1308a3e81fmshc5c7805a1477572p1ac776jsn696bc69cace6"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return render(request, "IndexCrypto.html", {'Data': response.json()["data"]})

def DetailedCrypto(request, uuid):
    url = "https://coinranking1.p.rapidapi.com/coin/"+uuid

    querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"24h"}

    headers = {
    'x-rapidapi-host': "coinranking1.p.rapidapi.com",
    'x-rapidapi-key': "1308a3e81fmshc5c7805a1477572p1ac776jsn696bc69cace6"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    ohlcurl = "https://coinranking1.p.rapidapi.com/coin/"+uuid+"/ohlc"
    ohlc = requests.request("GET", ohlcurl, headers=headers, params={"referenceCurrencyUuid":"yhjMzLPhuIDl","interval":"day", "limit":"1"})
    ohlc = ohlc.json()

    ohlc = ohlc["data"]["ohlc"][0]

    return render(request, "DetailedCrypto.html", {'Data': response.json()["data"]["coin"], "OHLCData": ohlc})

def MarketsCrypto(request, uuid):
    url = "https://coinranking1.p.rapidapi.com/coin/"+uuid+"/markets"

    querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","limit":"50","offset":"0","orderBy":"24hVolume","orderDirection":"desc"}

    headers = {
    'x-rapidapi-host': "coinranking1.p.rapidapi.com",
    'x-rapidapi-key': "1308a3e81fmshc5c7805a1477572p1ac776jsn696bc69cace6"
    }
    marketresponse = requests.request("GET", url, headers=headers, params=querystring)
    return render(request, "DetailedCrypto.html", {'MarketData': marketresponse.json()["data"]})