from pytest_factoryboy import register

from tests.factories import RoomFactory, UserFactory, BookingFactory

pytest_plugins = "tests.fixtures"

register(RoomFactory)
register(UserFactory)
register(BookingFactory)
