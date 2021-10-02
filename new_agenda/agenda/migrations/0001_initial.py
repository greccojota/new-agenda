# Generated by Django 3.2.7 on 2021-09-21 19:08

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
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('dt_evento', models.DateTimeField(verbose_name='Data do Evento')),
                ('dt_criacao', models.DateTimeField(auto_now=True, verbose_name='Data da Criação')),
                ('local', models.CharField(blank=True, max_length=100, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'evento',
            },
        ),
    ]
