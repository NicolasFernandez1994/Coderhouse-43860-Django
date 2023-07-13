from django.shortcuts import render

# Create your views here.


def home(request):
    contexto = {"app": "Nosotros"}
    return render(request, "http://127.0.0.1:8000/Nosotros/index.html", contexto)
