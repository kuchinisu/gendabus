from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.

def index(request):
    
    #template = loader.get_template("Rastreo/index.html")
    json_url = '/static/json/redT.json'
    camion_icon = '/static/img/icon/camion_ns.png'

    return render(request, 'index.html', {'json_url': json_url})