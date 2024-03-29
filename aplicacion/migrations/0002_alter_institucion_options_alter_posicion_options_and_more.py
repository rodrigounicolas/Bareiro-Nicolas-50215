# Generated by Django 5.0.2 on 2024-03-10 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='institucion',
            options={'ordering': ['nombre'], 'verbose_name': 'Institucion', 'verbose_name_plural': 'Institucion'},
        ),
        migrations.AlterModelOptions(
            name='posicion',
            options={'ordering': ['equipo'], 'verbose_name': 'Posicion', 'verbose_name_plural': 'Posicion'},
        ),
        migrations.AlterModelOptions(
            name='tablagoleadores',
            options={'ordering': ['jugador'], 'verbose_name': 'TablaGoleadores', 'verbose_name_plural': 'TablaGoleadores'},
        ),
        migrations.AlterField(
            model_name='institucion',
            name='direccion',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='institucion',
            name='nombre',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='posicion',
            name='equipo',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='tablagoleadores',
            name='jugador',
            field=models.CharField(max_length=60),
        ),
    ]