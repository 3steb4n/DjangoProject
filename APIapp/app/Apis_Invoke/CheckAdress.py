from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import requests
from BaseFile import generate_request

def returnCheckAdress(request):
    apiParameters = {
        'api_key' : '95e72c3491c419b628e86626d39709d265ae91cd'
    }
    responseRe = generate_request('https://faucetpay.io/api/v1/checkaddress', apiParameters)

    if responseRe:
        responseServiceCheckAdress = {
            "status" : responseRe.get('status'),
            "message" : responseRe.get('message'),
            "currencies" : responseRe.get('currency'),
            "balance" : responseRe.get('balance')
        }
    return render(request, 'CheckAdress.py', responseServiceCheckAdress)