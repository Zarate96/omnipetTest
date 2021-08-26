from django.shortcuts import render,redirect
from .models import Ciudades, Distancias, Zonas, Tarifas
from django.contrib import messages

# Create your views here.

def home(request):
    ciudades = Ciudades.objects.all()
    context = {'ciudades':ciudades}
    return render(request, 'pages/home.html', context)

def info(request):
    ciudades = Ciudades.objects.all()
    distancias = Distancias.objects.all()
    if request.method == 'POST':
        origenRe = request.POST['origen']
        destinoRe = request.POST['destino']
        alto = request.POST['alto']
        ancho = request.POST['ancho']
        largo = request.POST['largo']
        peso = request.POST['peso']

        if origenRe == destinoRe:
            messages.error(request, 'No se puede realizar el envio a una misma ciudad') 
            return redirect('home')
            
        origen = Ciudades.objects.get(nombre=origenRe)
        destino = Ciudades.objects.get(nombre=destinoRe)

        if origen and destino:
            distancia = Distancias.objects.filter(
                ciudad1=origen.id
            ).filter(
                ciudad2=destino.id
            ).distinct()
        
            distancia = distancia[0].distancia

        if distancia:
            zona = Zonas.objects.filter(min__lte=distancia).filter(max__gte=distancia)
            zona = zona[0].categoria
        
        pesovolumetrico = round((int(largo) * int(ancho) * int(alto)) / 5000)
        pesoreal = round(int(peso))
        
        pesoAbsoluto = 0
        if pesovolumetrico >= pesoreal and pesovolumetrico <= 70:
            pesoAbsoluto = pesovolumetrico
        else:
            pesoAbsoluto = pesoreal
        
        if pesoAbsoluto > 70 and pesoreal > 70:
            messages.error(request, 'Más de 70 kilos volumetricos no se puede realizar el envio')
            return redirect('home')
    
        tarifa1 = Tarifas.objects.filter(
            proveedor=1
        ).filter(
            kg__gte=pesoAbsoluto
        ).filter(
            zona=zona
        )

        tarifa2 = Tarifas.objects.filter(
            proveedor=2
        ).filter(
            kg__gte=pesoAbsoluto
        ).filter(
            zona=zona
        )

        tarifa3 = Tarifas.objects.filter(
            proveedor=3
        ).filter(
            kg__gte=pesoAbsoluto
        ).filter(
            zona=zona
        )
        
        proveedor1 = tarifa1[0].precio
        proveedor2 = tarifa2[0].precio
        proveedor3 = tarifa3[0].precio
                
        tarifas = [tarifa1, tarifa2, tarifa3]
        menor = tarifas[0][0].precio
        tarifaMasBaja= tarifa1
        for tarifa in tarifas:
            if tarifa[0].precio < tarifaMasBaja[0].precio:
                tarifaMasBaja=tarifa
        
        mejorPro = tarifaMasBaja[0].proveedor

        context = {
            'ciudades':ciudades,
            'distancia': distancia,
            'pesovolumetrico': pesovolumetrico,
            'pesoreal': pesoreal,
            'alto': alto,
            'ancho': ancho,
            'largo': largo, 
            'zona': zona,
            'origen': origenRe,
            'destino': destinoRe,
            'proveedor1': proveedor1,
            'proveedor2': proveedor2,
            'proveedor3': proveedor3,
            'menor':menor,
            'mejorPro': mejorPro,
        }

        return render(request, 'pages/home.html', context)

