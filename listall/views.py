from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
from .form import Update
from .models import Item, Category
# Create your views here.

def index(request):

    context = {'items': Item.objects.all() }
    return render(request, 'listall/index.html', context)
    
def category_index(request):
    """
    context = {
            'Categories': Category.objects.all(),
            'CategoryItems': [cat.item_set.all() for cat in Category.objects.all()],
            }
    """
    context = {}
    Category_Item = {}

    for c in Category.objects.all():
        Category_Item[c.name] = [ i for i in c.item_set.all()]
    
    context['CategoryItem'] = Category_Item

    return render(request, 'listall/category_index.html', context)

def new_addition(request):
    new_items = Item.objects.order_by('-id')[:3]
    #new_items = new_items[::-1]
    context = {
            'items': new_items,
            }
    return render(request, 'listall/new_additions.html', context)

def Request(request):
    items = Item.objects.all()
    return render(request,'additem.html',{'items':items})

def Add(request): 
    items = Item.objects.all()
    if request.method=='POST':
        form = Update(request.POST)
        if form.is_valid():
            item = form.save()    
        return redirect('Add')
    else:
        form = Update()
    return render(request,'request.html',{'form':form})
