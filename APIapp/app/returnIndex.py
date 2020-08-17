from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import requests


def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def returnIndex(request, params={
    'api_key' : '5b8a92b6414f88d358bc39e8db7de2fef64417b6'

}):
    responseRe = generate_request('https://faucetpay.io/api/v1/currencies', params)

    if responseRe:
        statusService = {
            "context" : responseRe.get('status')
        }

    return render(request, 'index.html', statusService) #Anotar la ruta completa en settings/TEMPLATES - DIRS
