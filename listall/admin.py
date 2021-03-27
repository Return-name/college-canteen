from django.contrib import admin

from .models import Item, Category

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    fields = ['name','price','quantity','image','image_tag',]
    readonly_fields = ['image_tag']

admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
