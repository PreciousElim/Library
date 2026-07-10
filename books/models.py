from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, unique=True)
    published_date = models.DateField(blank=True,null=True)
    is_available = models.BooleanField(default=True)
    
    class Meta:
         ordering = ['title']
    
    def __str__(self):
        return self.title
# Create your models here.
