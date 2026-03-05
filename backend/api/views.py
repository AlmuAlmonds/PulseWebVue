from django.contrib.auth.hashers import check_password
from django.core import signing
from django.core.signing import BadSignature, SignatureExpired
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import UserSignupSerializer


TOKEN_SIGNER = signing.TimestampSigner(salt='pulse-admin-auth')
TOKEN_MAX_AGE_SECONDS = 60 * 60 * 8


def _build_auth_payload(user):
    role_id = getattr(user, 'role_id', None)
    return {
        'message': 'Login successful',
        'user_id': user.id,
        'role_id': role_id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'token': TOKEN_SIGNER.sign(str(user.id))
    }


def _get_user_from_bearer(request):
    auth_header = request.headers.get('Authorization', '')
    if not auth_header.startswith('Bearer '):
        return None, Response({'error': 'Missing bearer token'}, status=status.HTTP_401_UNAUTHORIZED)

    token = auth_header.split(' ', 1)[1].strip()
    if not token:
        return None, Response({'error': 'Missing bearer token'}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        user_id = TOKEN_SIGNER.unsign(token, max_age=TOKEN_MAX_AGE_SECONDS)
    except SignatureExpired:
        return None, Response({'error': 'Token expired'}, status=status.HTTP_401_UNAUTHORIZED)
    except BadSignature:
        return None, Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return None, Response({'error': 'Invalid token user'}, status=status.HTTP_401_UNAUTHORIZED)

    return user, None


@api_view(['POST'])
def signup(request):
    serializer = UserSignupSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request):
    email = request.data.get("email")
    password = request.data.get("password")

    if not email or not password:
        return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    if not check_password(password, user.password):
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    return Response(_build_auth_payload(user), status=status.HTTP_200_OK)


@api_view(['GET'])
def admin_dashboard(request):
    user, error_response = _get_user_from_bearer(request)
    if error_response:
        return error_response

    if user.role_id != 1:
        return Response({'error': 'Access denied. Admins only.'}, status=status.HTTP_403_FORBIDDEN)

    return Response(
        {
            'message': 'Admin dashboard access verified',
            'user_id': user.id,
            'role_id': user.role_id,
            'first_name': user.first_name,
            'last_name': user.last_name
        },
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
def dispatcher_dashboard(request):
    user, error_response = _get_user_from_bearer(request)
    if error_response:
        return error_response

    if user.role_id != 2:
        return Response({'error': 'Access denied. Dispatch only.'}, status=status.HTTP_403_FORBIDDEN)

    return Response(
        {
            'message': 'Dispatch dashboard access verified',
            'user_id': user.id,
            'role_id': user.role_id,
            'first_name': user.first_name,
            'last_name': user.last_name
        },
        status=status.HTTP_200_OK
    )