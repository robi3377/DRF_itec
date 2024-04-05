from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth.models import User
from .models import Post

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class  UserAuth(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # token, _ = Token.objects.get_or_create(user=user)
            # token = Token.objects.get(user=user)
            return Response({'token': 'merge'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Autentificare invalidă'}, status=status.HTTP_401_UNAUTHORIZED)


# class(generics.ListAPIView):
#     serializer_class = PostSerializer
#     queryset = User.objects.all()
    

class UserCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
