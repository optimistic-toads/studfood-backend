# Generated by Django 3.1.3 on 2020-12-10 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_productinorder'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductInOrder',
        ),
    ]
