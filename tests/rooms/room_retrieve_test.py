import pytest


@pytest.mark.django_db
def test_retrieve_room(client, room):
    expected_response = {
        "id": room.pk,
        "number": '1',
        "price": 100,
        "beds": 1
    }

    response = client.get(
        f"/rooms/{room.pk}/"
    )

    assert response.status_code == 200
    assert response.data == expected_response
