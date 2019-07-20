from django.contrib import admin
from .models import Detail, Product

class DetailAdmin(admin.ModelAdmin): #1:52
    list_display = ('id', 'abv')

# Register your models here.

admin.site.register(Detail, DetailAdmin)
admin.site.register(Product)