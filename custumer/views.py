from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny ,SAFE_METHODS,BasePermission, IsAuthenticatedOrReadOnly,IsAuthenticated,IsAdminUser,DjangoModelPermissions
from .serializers import*
from .models import *
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import generics
from django.http import HttpResponseGone,JsonResponse
import jwt,datetime
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view

# Create your views here.

class ListCreat(generics.ListCreateAPIView):
    queryset=NewUser.objects.all()
    permission_classes=[AllowAny]
    serializer_class=UserSerializer

class ListCreatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=NewUser.objects.all()
    permission_classes=[AllowAny]
    serializer_class=UserSerializer

class RecensementView(APIView):
    def get(self,request):
        user=NewUser.objects.get(user_name=request.user)
        serializer_context = {'request': request}
        user_data=UserSerializer(user,context=serializer_context).data
        return Response(user_data)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_name'] = user.user_name
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



# class LoginView(APIView):
#     def post(self,request):
#         email=request.data['email']
#         password=request.data['password']
#         user=NewUser.objects.filter(email=email).first()
#         if user is None:
#             raise AuthenticationFailed('User not found')
#         if not user.check_password(password):
#             raise AuthenticationFailed('Incorrect Password')
#         payload={
#             'id':user.id,
#             'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=1),
#             'iat':datetime.datetime.utcnow()
#             }
#         token =jwt.encode(payload, 'secret',algorithm='HS256')
#         response =Response()
#         response.set_cookie(key='jwt',value=token,httponly=True)
#         response.data ={
#             'jwt':token
#         }
#         return response

# class LogoutView(APIView):
#     def post(self, request):
#         response=Response()
#         response.delete_cookie('jwt')
#         response.data ={
#             'message':'success'
#         }
#         return response


