# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Client, Calendario, Tramite


class TramiteInline(admin.TabularInline):
    model = Tramite


class CalendarioAdmin(admin.ModelAdmin):
    list_display = ("year", "mes", "tramites")
    list_filter = ("year", "mes", "tramites")
    search_fields = ("year", "mes", "tramites")
    inline = [TramiteInline]


admin.site.register(Client)
admin.site.register(Tramite)
admin.site.register(Calendario, CalendarioAdmin)
