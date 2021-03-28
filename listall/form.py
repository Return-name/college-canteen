from .models import Item
from django import forms 
class Update(forms.ModelForm):
    name = forms.CharField(max_length = 100)
    price = forms.IntegerField()
    quantity = forms.IntegerField()
    #image = forms.ImageField()

    class Meta:
        model = Item
        fields = ['name','price','quantity']
