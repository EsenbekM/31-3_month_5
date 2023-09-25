from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from users.serializers import LoginSerializer, RegisterSerializer, UserSerializer


@api_view(['POST'])
def register(request):
    # 0 - валидация
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    # 1 - создать пользователя
    user = User.objects.create_user(is_active=False, **serializer.data)

    # 2 - создать токен
    token, created = Token.objects.get_or_create(user=user)


    return Response(
        {'token': token.key, 'data': serializer.data}, 
        status=201
    )

@api_view(['POST'])
def login(request):
    # 0 - валидация
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    # serializer.data -> {'username': 'admin', 'password': 'admin'}

    # 2 - найти пользователя в базе данных
    user = authenticate(**serializer.data) # None or User
    
    if user:
        # 3 - создать токен
        token, created = Token.objects.get_or_create(user=user) # (token, True/False)
        
        # 4 - вернуть токен
        return Response({'token': token.key})

    return Response({'ERROR': 'WRONG CREDENTIALS'}, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()
    return Response(
        {'message': 'You have been successfully logged out.'},
        status=200
    )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    serializer = UserSerializer(user)

    return Response(
        {'data': serializer.data},
        status=200
    )
