# Generated by Django 4.0.6 on 2022-07-13 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_anexo_delete_fichaproyecto'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='programa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.proyecto', verbose_name='Programa'),
        ),
    ]
