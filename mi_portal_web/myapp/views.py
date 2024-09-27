from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Bienvenido a tu pagina")
    return render(request,'myapp/home.html')

def about(request):
    # return HttpResponse("Acerca de esta pagina")
    return render(request,'myapp/about.html')

def contact(request):
    return render(request,'myapp/contact.html')

def portafolio(request):
    projects = [
        {'name':" Pagina de Restaurante", 'description': 'Proyecto para cadena de restuarantes mexicanos','image':'images/img1.jpg','url': 'https://antonias.us/'},
        {'name':" Pagina de Inmobiliarias", 'description': 'Proyecto para venta de casas','image':'images/img1.jpg','url': 'https://www.urbanhouse.com.mx/'},
        {'name':" Pagina de Escuela", 'description': 'Proyecto para escuela de Psicologia','image':'','url': 'https://www.impotlax.org/'},
    ]
    return render(request,'myapp/portafolio.html', {'projects': projects})

# Create your views here.
