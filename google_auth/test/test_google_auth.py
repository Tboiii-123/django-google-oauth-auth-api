import pytest
from unittest.mock import patch
from django.urls import reverse


@pytest.mark.django_db
@patch(
    "google_auth.services.GoogleAuthService.verify_google_token"
)
@patch(
    "google_auth.services.GoogleAuthService.create_or_update_user"
)
def test_google_login_success(
    mock_create_user,
    mock_verify_token,
    api_client,
    user
):
    mock_verify_token.return_value = {
        "email": user.email
    }

    mock_create_user.return_value = user

    response = api_client.post(
        reverse("google-login"),
        {
            "id_token": "fake-google-token"
        },
        format="json"
    )

    assert response.status_code == 200
    assert response.data["status"] is True
    assert (
        response.data["message"]
        == "Google login successful"
    )

    assert "tokens" in response.data
    assert "access" in response.data["tokens"]
    assert "refresh" in response.data["tokens"]



#Invalid google token
@pytest.mark.django_db
@patch(
    "google_auth.services.GoogleAuthService.verify_google_token"
)
def test_google_login_invalid_token(
    mock_verify_token,
    api_client
):
    mock_verify_token.side_effect = ValueError(
        "Invalid Google token"
    )

    response = api_client.post(
        reverse("google-login"),
        {
            "id_token": "bad-token"
        },
        format="json"
    )

    assert response.status_code == 400
    assert response.data["status"] is False
    assert (
        response.data["message"]
        == "Invalid Google token"
    )


    #Missing tokne validation

@pytest.mark.django_db
def test_google_login_without_token(
    api_client
):
    response = api_client.post(
        reverse("google-login"),
        {},
        format="json"
    )

    assert response.status_code == 400
    assert "id_token" in response.data