from django.db.models import QuerySet
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from rooms.filters import RoomFilter
from rooms.models import Room, Booking
from rooms.permissions import IsSuperuser
from rooms.serializers import RoomSerializer, BookingSerializer


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (AllowAny, )
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RoomFilter

    def _sort_queryset(self, queryset: QuerySet) -> QuerySet:
        sort_field: str = self.request.GET.get('sort_field', None)
        if sort_field:
            queryset = queryset.order_by(sort_field)
        return queryset

    def get_queryset(self):
        if self.action == 'list':
            queryset: QuerySet = self._sort_queryset(Room.objects.all())

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
