# Generated by Django 3.2 on 2022-07-29 23:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('cancel_order', 'Can cancel order')]},
        ),
    ]