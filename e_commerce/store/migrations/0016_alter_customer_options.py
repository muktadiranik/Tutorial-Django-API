# Generated by Django 3.2 on 2022-07-30 22:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('store', '0015_auto_20220730_0504'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['user__first_name', 'user__last_name'],
                     'permissions': [('view_history', 'Can view history')]},
        ),
    ]
