# Generated by Django 3.1.3 on 2020-12-11 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20201122_1659'),
        ('order', '0008_auto_20201211_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]
