from datetime import datetime
from django.db.models import Q, Count, QuerySet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from rooms.models import Room, Booking
from rooms.permissions import IsSuperuser
from rooms.serializers import RoomSerializer, BookingSerializer


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (AllowAny, )

    def _filter_queryset(self, queryset: QuerySet) -> QuerySet:
        price_from: str = self.request.data.get('price_from', None)
        price_up_to: str = self.request.data.get('price_up_to', None)
        if price_from:
            price_from: int = int(price_from)
            queryset = queryset.filter(
                price__gte=price_from,
            )
        if price_up_to:
            price_up_to: int = int(price_up_to)
            queryset = queryset.filter(
                price__lte=price_up_to,
            )

        beds: str = self.request.data.get('beds', None)
        if beds:
            beds: int = int(beds)
            queryset = queryset.filter(
                beds=beds,
            )
        return queryset

    def _sort_queryset(self, queryset: QuerySet) -> QuerySet:
        sort_field: str = self.request.GET.get('sort_field', None)
        if sort_field:
            queryset = queryset.order_by(sort_field)
        return queryset

    def _booking_filter(self, queryset: QuerySet) -> QuerySet:
        check_in: str = self.request.data.get("check_in", None)
        check_out: str = self.request.data.get("check_out", None)
        if check_in and check_out:
            check_in: datetime = datetime.strptime(check_in, '%Y-%m-%d')
            check_out: datetime = datetime.strptime(check_out, '%Y-%m-%d')

            booking_q: Q = Q(booking__check_in__range=(check_in, check_out))
            booking_q |= Q(booking__check_out__range=(check_in, check_out))
            booking_q |= (Q(booking__check_in__lte=check_in) & Q(booking__check_out__gte=check_out))

            queryset = queryset.annotate(bookings=Count('booking', filter=booking_q)).filter(bookings=0)

        return queryset

    def get_queryset(self):
        if self.action == 'list':
            queryset: QuerySet = self._filter_queryset(Room.objects.all())
            queryset = self._sort_queryset(queryset)
            queryset = self._booking_filter(queryset)

            return queryset

        return super().get_queryset()

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy', 'partial_update']:
            return (IsSuperuser(), )

        return super().get_permissions()


class BookingViewSet(ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
