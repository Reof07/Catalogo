# Generated by Django 3.0.7 on 2020-12-01 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0006_delete_categorias'),
    ]

    operations = [
        migrations.AddField(
            model_name='tienda',
            name='banner_tienda',
            field=models.ImageField(blank=True, null=True, upload_to='banner'),
        ),
    ]
