# Generated by Django 4.1.4 on 2022-12-31 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='CPF',
        ),
        migrations.RemoveField(
            model_name='users',
            name='CRM',
        ),
        migrations.RemoveField(
            model_name='users',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='users',
            name='endereco',
        ),
        migrations.RemoveField(
            model_name='users',
            name='telefone',
        ),
    ]