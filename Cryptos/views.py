from django.shortcuts import render
import requests

def IndexCrypto(request):
    data = requests.request("GET", "http://127.0.0.1:8000/static/Coins.json")
    return render(request, "IndexCrypto.html", {'Data':data.json()["data"]["coins"]})