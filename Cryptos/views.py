from django.shortcuts import render,redirect
from django.urls import reverse
import requests
import json

def Home(request):
    return render(request, "Home.html")

def RedirectCrypto(request):
    return redirect(reverse("CryptoIndex", args=(1,)))

def IndexCrypto(request, page):
    url = "https://coinranking1.p.rapidapi.com/coins"

    querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"24h","orderBy":"marketCap","orderDirection":"desc","limit":"50","offset":str((page-1)*50)}

    headers = {
    'x-rapidapi-host': "coinranking1.p.rapidapi.com",
    'x-rapidapi-key': "1308a3e81fmshc5c7805a1477572p1ac776jsn696bc69cace6"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    return render(request, "IndexCrypto.html", {'Data': response["data"], 'MaxPage': int(response["data"]["stats"]["totalCoins"]/50), 'UrlPage': int(page)})


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