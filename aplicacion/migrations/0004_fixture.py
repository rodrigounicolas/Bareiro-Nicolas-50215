# Generated by Django 5.0.2 on 2024-03-24 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_goleador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.CharField(max_length=60)),
                ('vs', models.CharField(max_length=60)),
                ('visitante', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=60)),
            ],
        ),
    ]