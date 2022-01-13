from django.shortcuts import render
import requests
import json

def IndexCrypto(request):
    data = requests.request("GET", "http://127.0.0.1:8000/static/Coins.json")
    data = data.json()["data"]["coins"]
    return render(request, "IndexCrypto.html", {'Data': data})

def DetailedCrypto(request, uuid):
    response = requests.request("GET", "http://127.0.0.1:8000/static/CoinCall.json")
    return render(request, "DetailedCrypto.html", {'Data': response.json()["data"]["coin"]})