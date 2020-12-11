from django import forms
from .models import Producto, Tienda

class Product_forms(forms.ModelForm):

    class Meta():
        model= Producto
        fields= ('nombre', 'presio', 'descripcion', 'img',
            'delivery', 'pick_up',)

class Tienda_forms(forms.ModelForm):

    class Meta:
        model = Tienda
        fields= ('nombre', 'correo', 'rif', 'direccion',
            'telf', 'logo', 'descripcion', 'banner_tienda')