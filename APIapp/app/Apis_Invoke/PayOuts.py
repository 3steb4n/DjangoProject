from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import requests
from APIapp.app.Apis_Invoke.BaseFile import generate_request

def returnPayOut(request):
    apiParameters = {
        'api_key' : '95e72c3491c419b628e86626d39709d265ae91cd', #Parametro obligatorio
        'currency' : '', #Parametro opcional
        'count' : '' #Parametro opcional
    }
    responseRe = generate_request('https://faucetpay.io/api/v1/payouts', apiParameters)

    if responseRe:
        responseServicePayOuts = {
            "status" : responseRe.get('status'),
            "message" : responseRe.get('message'),
            "rewards_to" : responseRe.get('rewards')
        }
    return render(request, 'PayOuts.html', responseServicePayOuts)
