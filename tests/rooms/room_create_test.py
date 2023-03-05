import pytest


@pytest.mark.django_db
def test_create_selection(client, room, user_token):
    expected_response = {
        "detail": "You are not a superuser."
    }

    response = client.post(
        "/rooms/",
        data=room,
        content_type="application/json",
        HTTP_AUTHORIZATION="Bearer " + user_token
    )

    assert response.status_code == 403
    assert response.data == expected_response
