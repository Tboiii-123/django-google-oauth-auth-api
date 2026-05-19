import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_authenticated_user_can_get_profile(
    authenticated_client,
    user
):
    response = authenticated_client.get(
        reverse("user-detail")
    )

    assert response.status_code == 200
    assert response.data["email"] == user.email
    assert (
        response.data["user_name"]
        == user.user_name
    )


#: Unauthorized user
@pytest.mark.django_db
def test_unauthenticated_user_cannot_get_profile(
    api_client
):
    response = api_client.get(
        reverse("user-detail")
    )

    assert response.status_code == 401