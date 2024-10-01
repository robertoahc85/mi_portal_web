from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
 
class Event(models.Model):
    name = models.CharField(max_length=100)  
    description = models.TextField()  
    fecha =models.DateField()
    capacidad = models.IntegerField()
    
class Portafolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    link = models.URLField(blank=True, null=True)
    
class Testimonio(models.Model):
       nombre=models.CharField(max_length=150)
       testimonio=models.TextField()
       puesto=models.CharField(max_length=100)
       empresa=models.CharField(max_length=50)
  
    
def __str__(self):
       return self.name 
