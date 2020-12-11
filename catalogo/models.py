from django.db import models

# Create your models here.

class Tienda(models.Model):
    nombre = models.CharField(max_length=150)
    correo = models.EmailField()
    rif = models.CharField(max_length=8,  null=True, blank=True)
    direccion = models.CharField(max_length=200)
    telf = models.CharField(max_length=12, null=True, blank=True)
    logo = models.ImageField(upload_to='perfil', null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    banner_tienda= models.ImageField(upload_to='banner', null=True, blank=True)
    

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    YES = 'Si'
    NOT = 'No'
    entrega= [(YES, 'Si'),
        (NOT,'No')
        ]
    buscar= [(YES, 'Si'),
        (NOT,'No')
        ]
    nombre = models.CharField(max_length=50)
    presio = models.CharField(max_length=15)
    descripcion = models.TextField()
    img = models.ImageField(upload_to ='product')
    delivery = models.CharField(max_length=3,
        choices=entrega, default=YES) 
    pick_up= models.CharField(max_length=3,
        choices=buscar, default=YES)

    def __str__(self):
        return self.nombre
