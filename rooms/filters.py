from django.db.models import Q
from django_filters import rest_framework as filters

from rooms.models import Room


class RoomFilter(filters.FilterSet):
    price_from = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_up_to = filters.NumberFilter(field_name='price', lookup_expr='lte')

    booking = filters.DateFromToRangeFilter(field_name='booking', method='filter_booking')

    class Meta:
        model = Room
        fields = ['price', 'beds', 'booking']

    def filter_booking(self, queryset, name, value):
        check_in = value.start
        check_out = value.stop

        booking_q: Q = Q(booking__check_in__range=(check_in, check_out))
        booking_q |= Q(booking__check_out__range=(check_in, check_out))
        booking_q |= (Q(booking__check_in__lte=check_in) & Q(booking__check_out__gte=check_out))

        return queryset.exclude(booking_q)
