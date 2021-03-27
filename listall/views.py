from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Item, Category
# Create your views here.

def index(request):

    context = {'items': Item.objects.all() }
    return render(request, 'listall/index.html', context)
    
def category_index(request):
    context = {
            'Categories': Category.objects.all(),
            'CategoryItems': [cat.item_set.all() for cat in Category.objects.all()],
            }

    return render(request, 'listall/category_index.html', context)
