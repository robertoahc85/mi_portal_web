from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Bienvenido a tu pagina")
    return render(request,'myapp/home.html')

def about(request):
    # return HttpResponse("Acerca de esta pagina")
    return render(request,'myapp/about.html')

def contact(request):
    # return HttpResponse("Pagina de Contacto")
    return render(request,'myapp/contact.html')

# Create your views here.
