# Generated by Django 2.1.2 on 2018-11-08 23:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('codigoMascota', models.AutoField(primary_key=True, serialize=False)),
                ('nombreMascota', models.CharField(max_length=20)),
                ('razaMascota', models.CharField(default='', max_length=30)),
                ('descripcionMascota', models.CharField(default='', max_length=50)),
                ('estado', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perfil', models.CharField(default='Invitado', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('Administrador', 'Administrador'), ('Adoptante', 'Adoptante')),
            },
        ),
    ]
