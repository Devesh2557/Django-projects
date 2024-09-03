from django.db import models


# Create your models here.


class Blog(models.Model):
    image = models.ImageField(upload_to='media')
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=10000)
    date = models.DateField()
    
class Contact(models.Model):
    Name = models.CharField(max_length=10)
    Email = models.EmailField(max_length=50)
    Subject = models.CharField(max_length=50)
    Message = models.CharField(max_length=500) 
    
    

