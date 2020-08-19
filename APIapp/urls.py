"""APIapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from APIapp.app.returnIndex import returnIndex
from APIapp.app.Apis_Invoke.CheckAdress import returnCheckAdress
from APIapp.app.Apis_Invoke.PayOuts import returnPayOut
from APIapp.app.Apis_Invoke.SendPaymount import returnSendPayMount

urlpatterns = [
    path('', returnIndex),
    path(r'^/PayOuts', returnPayOut, name ='returnPayOut'),
    path(r'^/CheckAddres', returnCheckAdress, name = 'returnCheckAdress'),
    path(r'^/SendPayMount', returnSendPayMount, name = 'returnSendPayMount')
]
