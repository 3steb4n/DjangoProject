from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def returnIndex(request):
    informationApi = {}
    return render(request, 'index.html', informationApi) #Anotar la ruta completa en settings/TEMPLATES - DIRS
