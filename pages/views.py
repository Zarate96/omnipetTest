from django.shortcuts import render
from .models import Ciudades
# Create your views here.

def home(request):
    ciudades = Ciudades.objects.all()
    context = {'ciudades':ciudades}
    return render(request, 'pages/home.html', context)

def info(request):
    if request.method == 'POST':
        pass