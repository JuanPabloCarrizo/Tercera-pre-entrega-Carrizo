# Generated by Django 4.2.5 on 2023-10-18 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GaleriaApp', '0004_alter_artista_foto_alter_galeria_foto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='obra',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarios_obra', to='GaleriaApp.obra'),
        ),
    ]
