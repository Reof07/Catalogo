from django.shortcuts import  get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Tienda, Producto
from .forms import Product_forms, Tienda_forms

# Create your views here.

# retorna una lista de productos. 
class HomeView(generic.ListView):
    template_name = 'catalogo/home.html'
    context_object_name = 'list_product'

    def get_queryset(self):
        return Producto.objects.all() #NOTA: ordenar por fecha 

#Crear tienda
def crear_tienda(request):
    if request.method == 'POST':
        form = Tienda_forms(request.POST, request.FILES)    
        if form.is_valid():
            form.save()
        tienda_obj = form.instance    
        return render(request, 'catalogo/create_tienda_form.html', {'form':form, 'product_obj':tienda_obj})
    else:
        form = Tienda_forms()
    return render(request, 'catalogo/create_tienda_form.html',{'form':form} )  


#Crea un formulario para productos. (mejorar con vistas basadas en clases)
def crear_producto(request):
    if request.method == 'POST':
        form = Product_forms(request.POST, request.FILES)    
        if form.is_valid():
            form.save()
        product_obj = form.instance    
        return render(request, 'catalogo/create_product_form.html', {'form':form, 'product_obj':product_obj})
    else:
        form = Product_forms()
    return render(request, 'catalogo/create_product_form.html',{'form':form} )  

# detalles del producto.
class DetailView(generic.DetailView):
    model = Producto
    template_name = 'catalogo/detail.html'
    context_object_name = 'product'
 
# returna la vista de contacto. 
def contacto(request):
    contact = Tienda.objects.get()
    context = {'contacto':contact }
    return render(request, 'catalogo/contacto.html', context)

  
