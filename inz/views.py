from django.http import HttpResponse
#from django.temeplate import loader
from django.shortcuts import render

def index(request):
   #temeplate=loader.get_temeplate("index.html")
    return render(request, "inz/index.html")
    return render(request, "inz/kontakt.html")
    return render(request, "inz/Menu.html")
    return render(request, "inz/O_nas.html")
    return render(request, "inz/Pokoje.html")
    return render(request, "inz/warianty_wyzywienia.html")