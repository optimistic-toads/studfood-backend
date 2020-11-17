# Generated by Django 3.1.3 on 2020-11-17 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maindishes',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='Amount'),
        ),
        migrations.AlterField(
            model_name='maindishes',
            name='weight',
            field=models.PositiveIntegerField(verbose_name='Weight'),
        ),
    ]
