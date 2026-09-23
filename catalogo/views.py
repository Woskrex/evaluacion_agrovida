from django.shortcuts import render

# Create your views here.
def vista_detalle(request):
    return render(request, 'detalle.html')

def vista_productos(request):
    return render(request, 'productos.html')

def vista_contacto(request):
    return render(request, 'contacto.html')