from django.shortcuts import render

# Create your views here.

def home(request):
    contexto = {"app": "Faq" }
    return render(request, "Faq/index.html", contexto)