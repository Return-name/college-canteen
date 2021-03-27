from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Item
# Create your views here.

def index(request):
    output = "<html><center>Hello. Here is the list of all items in the canteen<br>"
    items = Item.objects.all()
    output += "<table border=2><th>Image</th><th>Name</th><th>Price</th><th>Quantity</th>"
    for i in items:
        output += "<tr>"
        if i.image:
            output += "<td>"+i.image_tag()+"</td>"
        else:
            output += "<td>[Img Not Avl]</td>"
        output += "<td>"+i.name + "</td><td>" + str(i.price) + "</td><td>" + str(i.quantity) + "</td></tr>"
    output += "</table></center><html>";
    return HttpResponse(output)
