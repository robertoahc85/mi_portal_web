from django import forms
from .models import Contact, Event

class ContactForm(forms.ModelForm):
     class Meta:
        model = Contact
        fields = ['name','email', 'message']
        
class EventForm (forms.ModelForm):
   class Meta:
      model = Event 
      fields =['name','description','fecha','capacidad']      
