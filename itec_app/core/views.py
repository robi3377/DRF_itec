from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth.models import User
from .models import Post, User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class  UserAuth(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        # user = authenticate(request, username=username, password=password)
        user = User.objects.filter(username=username, password=password).first()
        
        if user is not None:
            # token, _ = Token.objects.get_or_create(user=user)
            # token = Token.objects.get(user=user)
            return Response({'token': f'{username}, {password}'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': f'{username}, {password}'}, status=status.HTTP_401_UNAUTHORIZED)

class  UserCreate(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        # user = authenticate(request, username=username, password=password)
        user = User.objects.create(username=username, password=password, email=email)
        
        if user is not None:
            # token, _ = Token.objects.get_or_create(user=user)
            # token = Token.objects.get(user=user)
            return Response({'token': f'{username}, {password}'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': f'{username}, {password}'}, status=status.HTTP_401_UNAUTHORIZED)

from .serializers import LoginSerializer

from rest_framework.permissions import AllowAny

class LoginView(APIView):
    permission_classes = [AllowAny]  # Allow non-authenticated users to access this view

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class(generics.ListAPIView):
#     serializer_class = PostSerializer
#     queryset = User.objects.all()
    

# class UserCreate(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    
class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
