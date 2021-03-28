from .models import RequestItem
from django import forms 
class Update(forms.ModelForm):
    name = forms.CharField(max_length = 100)
    price = forms.IntegerField()

    class Meta:
        model = RequestItem
        fields = ['name','price']
