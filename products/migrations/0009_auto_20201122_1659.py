# Generated by Django 3.1.3 on 2020-11-22 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20201117_2111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='ingredients',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='cover_photo',
            new_name='photo',
        ),
    ]
