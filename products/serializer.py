from rest_framework import serializers


class MainDishesSerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length=100
    )

    cover_photo = serializers.ImageField()

    price = serializers.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    created_date = serializers.DateField(
    )

    updated_date = serializers.DateField(
    )

    quantity = serializers.IntegerField()

    weight = serializers.IntegerField()

    ingredients = serializers.CharField(
        max_length=200
    )
