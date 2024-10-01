from django import forms
from .models import Contact, Event,Portafolio,Testimonio

class ContactForm(forms.ModelForm):
     class Meta:
        model = Contact
        fields = ['name','email', 'message']
        
class EventForm (forms.ModelForm):
   class Meta:
      model = Event 
      fields =['name','description','fecha','capacidad']    
      
class PortafolioForm (forms.ModelForm):
   class Meta:
      model = Portafolio
      fields =['title','description','image','link']  

class TestimonioForm(forms.ModelForm):
   class Meta:
      model = Testimonio
      fields = ['nombre','testimonio','puesto', 'empresa']   
      
           
