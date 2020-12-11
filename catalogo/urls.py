from django.urls import path

from . import views

app_name= 'catalogo'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('contacto/', views.contacto, name='contacto'),
    path('crear-producto/', views.crear_producto, name='crear_product'),
    path('crear-tienda/', views.crear_tienda, name='crear_tienda'),
]