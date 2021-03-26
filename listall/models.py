from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    # itemno name price quantity
