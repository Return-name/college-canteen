from django.shortcuts import render
from django.http import HttpResponse

from .models import Item
# Create your views here.

def index(request):
    output = "<html><center>Hello. Here is the list of all items in the canteen<br>"
    items = Item.objects.all()
    output += "<table><th>Name</th><th>Price</th><th>Quantity</th>"
    for i in items:
        output += "<tr><td>"+i.name + "</td><td>" + str(i.price) + "</td><td>" + str(i.quantity) + "</td></tr>"
    output += "</table></center><html>";
    return HttpResponse(output)

