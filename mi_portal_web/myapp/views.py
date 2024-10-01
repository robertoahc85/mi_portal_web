from django.http import HttpResponse
from django.shortcuts import render,redirect
from .form import ContactForm ,EventForm , TestimonioForm
from .models import Event,Testimonio

def home(request):
    #return HttpResponse("Bienvenido a tu pagina")
    return render(request,'myapp/home.html')

def about(request):
    # return HttpResponse("Acerca de esta pagina")
    return render(request,'myapp/about.html')

def contact(request):
    if request.method == 'POST':
     form = ContactForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('home')
    else:
        form = ContactForm()
    return render(request,'myapp/contact.html',{'form': form})

def testimonail(request):
    # testimonail_data = [
    #     {'nombre':" Roberto", 'puesto':" CEO of M6.33 Tecnology", 'testimonio':"Excelente Servicio"},
    #     {'nombre':" Roberto", 'puesto':" CEO of M6.33 Tecnology", 'testimonio':"Excelente Servicio"},
    # ]
    testimonail_data = Testimonio.objects.all
    return render(request,'myapp/testimonail.html', {'testimonails': testimonail_data})

def testimonio_registro(request):
    if request.method == 'POST':
        form = TestimonioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonail_list')
    else: 
        form = TestimonioForm()
    return render(request, 'myapp/testimonio_registro.html',{'form':form})    

def portafolio(request):
    projects = [
        {'name':" Pagina de Restaurante", 'description': 'Proyecto para cadena de restuarantes mexicanos','image':'images/img1.jpg','url': 'https://antonias.us/'},
        {'name':" Pagina de Inmobiliarias", 'description': 'Proyecto para venta de casas','image':'images/img2.jpg','url': 'https://www.urbanhouse.com.mx/'},
        {'name':" Pagina de Escuela", 'description': 'Proyecto para escuela de Psicologia','image':'images/img3.jpg','url': 'https://www.impotlax.org/'},
    ]
    return render(request,'myapp/portafolio.html', {'projects': projects})

def event_register_view(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request,'myapp/event_register.html',{'form': form}) 

def event_list_view(request):
     events = Event.objects.all()  #Select * from Events   
     return render(request, 'myapp/event_list.html',{'events':events})
 
 
 #Crear el modelo para  portafolio y testimonio , 
 # crear el formulario alta de testimonios y portafolio
