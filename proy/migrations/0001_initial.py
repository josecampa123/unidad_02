# Generated by Django 3.2 on 2021-04-20 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organizadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sucarsal', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Juegos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('juego', models.CharField(max_length=200)),
                ('edades', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('foto', models.CharField(default='', max_length=200)),
                ('Organizadores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proy.organizadores')),
                ('Tienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proy.tienda')),
            ],
        ),
    ]