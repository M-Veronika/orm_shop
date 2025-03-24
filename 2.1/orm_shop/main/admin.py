from django.contrib import admin
from .models import Client, Car, Sale 

admin.site.register(Car)
admin.site.register(Sale)
admin.site.register(Client)

