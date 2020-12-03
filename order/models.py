from django.db import models
from products import models as product_model
from django.contrib.auth import get_user_model

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user',
        default=1
    )

    product = models.ManyToManyField(
        product_model.Product
    )

    created_date = models.DateTimeField(
        'Time',
        blank=True,
        null=True
    )
