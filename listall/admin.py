from django.contrib import admin

from .models import Item, Category, RequestItem

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    fields = ['name','price','quantity','image','image_tag','category']
    readonly_fields = ['image_tag']

admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(RequestItem)
