# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Client, Calendario, Tramite

admin.site.register(Client)
admin.site.register(Tramite)
admin.site.register(Calendario)
