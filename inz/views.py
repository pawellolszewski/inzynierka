from django.http import HttpResponse
#from django.temeplate import loader
from django.shortcuts import render

def index(request):
   #temeplate=loader.get_temeplate("index.html")
    return render(request, "inz/index.html")