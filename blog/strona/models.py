from django.db import models
from django.urls import reverse
from datetime import date,datetime
# Create your models here.

class Autor(models.Model):
    imie=models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    objects = models.Manager()
    def __str__(self):
        return self.imie
class Post(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=200)
    description = models.CharField(max_length=300,blank=True)
    Image= models.ImageField(upload_to=None,blank=True)
    data = models.DateField( auto_now_add=True)
    objects = models.Manager()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post-detail', args=(str(self.pk)))
