import factory

from rooms.models import Room, Booking
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("test")
    password = "test1234"


class RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Room

    number = 1
    price = 100
    beds = 1


class BookingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Booking

    room = 1
    user = 1
    check_in = "2022-10-10"
    check_out = "2022-11-10"
