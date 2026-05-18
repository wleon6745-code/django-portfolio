from django.shortcuts import render
from .models import Portfolio
from .models import Persona

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def portfolio(request):

    projects = Portfolio.objects.all()

    return render(request, "portfolio.html", {
        'projects': projects
    })

def contact(request):
    return render(request, 'contact.html')
def about(request):
    persona = Persona.objects.first()
    return render(request, "about.html", {
        'persona': persona
    })