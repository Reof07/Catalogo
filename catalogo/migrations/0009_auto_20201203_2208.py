# Generated by Django 3.0.7 on 2020-12-04 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0008_auto_20201203_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='delivery',
            field=models.CharField(choices=[('Si', 'Si'), ('No', 'No')], default='Si', max_length=3),
        ),
        migrations.AlterField(
            model_name='producto',
            name='pick_up',
            field=models.CharField(choices=[('Si', 'Si'), ('No', 'No')], default='Si', max_length=3),
        ),
    ]
