from django.db import models


class Product(models.Model):
    name = models.CharField(
        'Name',
        max_length=100
    )

    photo = models.ImageField(
        'Photo'
    )

    price = models.DecimalField(
        'Price',
        max_digits=5,
        decimal_places=2
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

    description = models.CharField(
        'Ingredients',
        max_length=200,
        blank=True,
        null=True
    )

    PRODUCT_TYPE_CHOICE = (
        ('main_dish', 'Main dish'), ('desert', 'Desert'), ('drink', 'Drink'), ('other_products', 'Other products')
    )

    type_of_product = models.CharField(
        max_length=50,
        choices=PRODUCT_TYPE_CHOICE,
        default='Main dish'
    )

    def __str__(self):
        return self.name
