from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import GoogleAuthSerializer
from .services import GoogleAuthService
from .throttles import LoginThrottle,MessageThrottle

@api_view(["POST"])
@permission_classes([AllowAny])
@throttle_classes([LoginThrottle])
def google_login(request):

    serializer = GoogleAuthSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)

    try:
        token = serializer.validated_data["id_token"]

        payload = GoogleAuthService.verify_google_token(token)

        user = GoogleAuthService.create_or_update_user(payload)

        refresh = (
            RefreshToken.for_user(user)
        )

        return Response(
            {
                "status": True,
                "message":
                "Google login successful",

                "user": {
                    "email": user.email,
                    "user_name": user.user_name,
                    "first_name": user.first_name,
                    "last_name":user.last_name,
                },

                "tokens": {
                "access": str(refresh.access_token),
                "refresh":str(refresh),
                }
            },
            status=status.HTTP_200_OK
        )

    except ValueError as e:
        return Response(
            {
                "status": False,
                "message": str(e)
            },
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@throttle_classes([MessageThrottle])
def user_detail(request):

    user = request.user

    return Response({
        "email": user.email,
        "first_name":
        user.first_name,
        "last_name":
        user.last_name,
        "user_name":
        user.user_name
    })