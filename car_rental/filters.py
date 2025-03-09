import django_filters
from .models import Car


class PriceFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(
        field_name="price_per_day", lookup_expr="gte"
    )
    max_price = django_filters.NumberFilter(
        field_name="price_per_day", lookup_expr="lte"
    )

    class Meta:
        model = Car
        fields = [
            "min_price",
            "max_price",
            "car_type",
            "seat_capacity",
            "is_available",
        ]
