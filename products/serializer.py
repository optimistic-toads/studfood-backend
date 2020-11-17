from rest_framework import serializers


class ProductsSerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length=100
    )

    cover_photo = serializers.ImageField()

    price = serializers.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    weight = serializers.IntegerField()

    ingredients = serializers.CharField(
        max_length=200
    )

    type_of_product = serializers.CharField(
        max_length=50,
    )
