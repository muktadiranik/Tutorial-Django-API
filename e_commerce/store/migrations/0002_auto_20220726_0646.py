# Generated by Django 3.2 on 2022-07-26 00:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='unit_price',
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='-'),
        ),
    ]
