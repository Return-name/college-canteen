from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="listall/static/listall/images/")
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def image_tag(self):
        path = self.image.url
        loc = path[1:].find('/')+1
        return mark_safe('<img src="' + path[loc:] + '" width="150" height="150" />')
    image_tag.short_description = 'Image'

class RequestItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name
