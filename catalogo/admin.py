from django.contrib import admin

from .models import Tienda, Producto

class TiendaAdmin(admin.ModelAdmin):
    list_display = ['nombre','telf','rif','correo']

class ProductoAdmin(admin.ModelAdmin):
    list_display= ['nombre', 'presio','descripcion', 'delivery','pick_up']    

# Register your models here.
admin.site.register(Tienda,TiendaAdmin)
admin.site.register(Producto, ProductoAdmin)