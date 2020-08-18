from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import requests
from APIapp.app.Apis_Invoke.BaseFile import generate_request

def returnCheckAdress(request):
    apiParameters = {
        'api_key' : '95e72c3491c419b628e86626d39709d265ae91cd', #Parametro requerido
        'address' : '', #Parametro requerido
        'currency' : '' #Parametro opcional
    }
    
    responseRe = generate_request('https://faucetpay.io/api/v1/checkaddress', apiParameters)

    if responseRe:
        if responseRe.get('status') != '200':
            responseServiceCheckAdress = {
            "responseRe" : responseRe.get('status'),
            "status" : responseRe.get('status'),
            "message" : responseRe.get('message')
            }
        else:
            responseServiceCheckAdress = {
            "responseRe" : responseRe.get('status'),
            "status" : responseRe.get('status'),
            "message" : responseRe.get('message'),
            "payout_user_hash" : responseRe.get('payout_user_hash')
            }
    return render(request, 'CheckAdress.html', responseServiceCheckAdress)