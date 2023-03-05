import pytest

from rooms.serializers import RoomSerializer
from tests.factories import RoomFactory


@pytest.mark.django_db
def test_room_list(client):
    rooms = RoomFactory.create_batch(10)

    expected_response = RoomSerializer(rooms, many=True).data

    response = client.get("/rooms/")

    assert response.status_code == 200
    assert response.data == expected_response
