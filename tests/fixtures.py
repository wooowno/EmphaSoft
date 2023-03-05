import pytest


@pytest.fixture
@pytest.mark.django_db
def user_token(client, django_user_model):
    username = 'test'
    password = 'test1234'

    django_user_model.objects.create_user(
        username=username, password=password
    )

    response = client.post(
        "/users/token/",
        {"username": username, "password": password},
        format='json'
    )

    return response.data["access"]
