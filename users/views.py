from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserLoginValidateSerializer, UserCreateSerializer


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    def post(self, request):
        serializer = UserLoginValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user is not None:
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            return Response(data={'key': token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED)

# @api_view(['POST'])
# def register(request):
#     serializer = UserCreateSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     User.objects.create_user(**serializer.validated_data)
#     return Response(status=status.HTTP_201_CREATED)

# @api_view(['POST'])
# def login(request):
# serializer = UserLoginValidateSerializer(data=request.data)
# serializer.is_valid(raise_exception=True)
# user = authenticate(**serializer.validated_data)
# if user is not None:
#     Token.objects.filter(user=user).delete()
#     token = Token.objects.create(user=user)
#     return Response(data={'key': token.key})
# return Response(status=status.HTTP_401_UNAUTHORIZED)
