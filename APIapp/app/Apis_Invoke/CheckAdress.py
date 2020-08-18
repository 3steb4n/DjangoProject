import requests
from BaseFile import generate_request

def returnCheckAdress():
    apiParameters = {
        'api_key' : '95e72c3491c419b628e86626d39709d265ae91cd'
    }
    responseRe = generate_request('https://faucetpay.io/api/v1/checkaddress', apiParameters)

    if responseRe:
        responseService = {
            "status" : responseRe.get('status'),
            "message" : responseRe.get('message'),
            "currencies" : responseRe.get('currency'),
            "balance" : responseRe.get('balance')
        }

    print(responseService)