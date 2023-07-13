from nturl2path import url2pathname
from django.shortcuts import render

# Create your views here.


def home(request):
    contexto = {"app": "Nosotros"}
    return render(request, url2pathname("Nosotros/index.html"), contexto)
