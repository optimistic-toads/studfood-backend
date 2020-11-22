from rest_framework import serializers


class ProductsListSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField(

    )

    name = serializers.CharField(
        max_length=100
    )

    photo = serializers.ImageField()

    price = serializers.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    weight = serializers.IntegerField()

    description = serializers.CharField(
        max_length=200
    )

    type_of_product = serializers.CharField(
        max_length=50,
    )
