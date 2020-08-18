from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import requests

def returnIndex(request):
    return render(request, 'index.html')