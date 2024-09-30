from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
 
class Event(models.Event):
    name = models.CharField(max_length=100)  
    description = models.TextField()  
    fecha =models.DateField()
    capacidad = models.IntegerField()
    
def __str__(self):
       return self.name 
