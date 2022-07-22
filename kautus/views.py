from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework import status
from .serializers import DocksItemSerializer
from .models import DocksItem
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
       
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        print(created,'aa')
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            "name":user.first_name
        })



# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    def get(self,request,*args,**kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer






class DocksItemViews(APIView):
    def post(self, request):
        serializer = DocksItemSerializer(data=request.data)
        print(serializer, '0900000000000000')
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)