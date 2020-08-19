import requests
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from APIapp.app.Apis_Invoke.BaseFile import generate_request

def returnSendPayMount(request):
    sendPayMontParameters = {
        'api_key' : '95e72c3491c419b628e86626d39709d265ae91cd', #Parametro obligatorio
        'amount' : '10', #Parametro obligatorio
        'to' : 'juangomez1947@outlook.com' #Parametro obligatorio
    }

    getJsonAPI = generate_request('https://faucetpay.io/api/v1/send', sendPayMontParameters)

    if getJsonAPI:
        sendValues = {
        'status' : getJsonAPI.get('status'),
        'message' : getJsonAPI.get('message'),
        'rate_limit_remaining' : getJsonAPI.get('rate_limit_remaining'),
        'currency' : getJsonAPI.get('currency'),
        'balance' : getJsonAPI.get('balance'),
        'balance_bitcoin' : getJsonAPI.get('balance_bitcoin'),
        'payout_id' : getJsonAPI.get('payout_id'),
        'payout_user_hash' : getJsonAPI.get('payout_user_hash')
         }
    return render(request, 'SendPaymount.html', sendValues)
