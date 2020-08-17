from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import requests


def generate_request(url, auth):
    response = requests.post(url, auth)

    if response.status_code == 200:
        return response.json()

def returnIndex(request):
    apiParameters = {
        'api_key' : '95e72c3491c419b628e86626d39709d265ae91cd'
    }
    responseRe = generate_request('https://faucetpay.io/api/v1/getbalance', apiParameters)

    if responseRe:
        statusService = {
            "status" : responseRe.get('status'),
            "message" : responseRe.get('message'),
            "currencies" : responseRe.get('currency'),
            "balance" : responseRe.get('balance')
        }

    return render(request, 'index.html', statusService) #Anotar la ruta completa en settings/TEMPLATES - DIRS
