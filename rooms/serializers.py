from rest_framework import serializers

from rooms.models import Room, Booking


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        model = Booking
        fields = '__all__'
