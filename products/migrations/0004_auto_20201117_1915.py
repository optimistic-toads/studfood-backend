# Generated by Django 3.1.3 on 2020-11-17 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20201117_1805'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MainDishes',
            new_name='MainDish',
        ),
    ]
