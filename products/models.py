from django.db import models


class MainDishes(models.Model):
    name = models.CharField(
        'Name',
        max_length=100
    )

    cover_photo = models.ImageField(
        'Photo'
    )

    price = models.DecimalField(
        'Price',
        max_digits=5,
        decimal_places=5
    )

    created_date = models.DateField(
        'Created Date',
        auto_now_add=True
    )

    updated_date = models.DateField(
        'Updated Date',
        auto_now=True
    )

    quantity = models.PositiveIntegerField(
        'Amount',
    )

    weight = models.PositiveIntegerField(
        'Weight',
    )

    ingredients = models.CharField(
        'Ingredients',
        max_length=200
    )
