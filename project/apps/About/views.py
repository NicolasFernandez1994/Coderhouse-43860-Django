from django.shortcuts import render

# Create your views here.

def home(request):
    contexto = {"app": "About" }
    return render(request, "about/index.html", contexto)