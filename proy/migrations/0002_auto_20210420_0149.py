# Generated by Django 3.1.6 on 2021-04-20 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juegos',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='organizadores',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tienda',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
