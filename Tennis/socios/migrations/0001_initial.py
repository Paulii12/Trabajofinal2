# Generated by Django 5.0.8 on 2024-08-20 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Socios',
            fields=[
                ('idSocio', models.AutoField(db_column='idSocio', primary_key=True, serialize=False)),
                ('DNI', models.IntegerField(verbose_name='DNI')),
                ('nom', models.CharField(max_length=50, verbose_name='Nombre y Apellido')),
                ('fechan', models.DateField(verbose_name='Fecha Nacimiento')),
                ('dire', models.CharField(max_length=50, verbose_name='Direccion')),
                ('cd', models.CharField(max_length=6, verbose_name='codigo postal')),
                ('tel', models.CharField(max_length=12, verbose_name='numero de telefono')),
            ],
        ),
    ]
