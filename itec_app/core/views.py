# from rest_framework import generics
# from .serializers import UserSerializer
# from django.contrib.auth.models import User
# from .models import Post, User

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.authtoken.models import Token
# from django.contrib.auth import authenticate

# class  UserAuth(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         # user = authenticate(request, username=username, password=password)
#         user = User.objects.filter(username=username, password=password).first()
        
#         if user is not None:
#             # token, _ = Token.objects.get_or_create(user=user)
#             # token = Token.objects.get(user=user)
#             return Response({'token': f'{username}, {password}'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': f'{username}, {password}'}, status=status.HTTP_401_UNAUTHORIZED)

# class  UserCreate(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         email = request.data.get('email')
#         # user = authenticate(request, username=username, password=password)
#         user = User.objects.create(username=username, password=password, email=email)
        
#         if user is not None:
#             # token, _ = Token.objects.get_or_create(user=user)
#             # token = Token.objects.get(user=user)
#             return Response({'token': f'{username}, {password}'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': f'{username}, {password}'}, status=status.HTTP_401_UNAUTHORIZED)

# from .serializers import LoginSerializer

# from rest_framework.permissions import AllowAny

# class LoginView(APIView):
#     permission_classes = [AllowAny]  # Allow non-authenticated users to access this view

#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             username = serializer.validated_data['username']
#             password = serializer.validated_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 token, created = Token.objects.get_or_create(user=user)
#                 return Response({'token': token.key})
#             else:
#                 return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # class(generics.ListAPIView):
# #     serializer_class = PostSerializer
# #     queryset = User.objects.all()
    

# # class UserCreate(generics.ListCreateAPIView):
# #     queryset = User.objects.all()
# #     serializer_class = UserSerializer
    
# class PostDetail(generics.RetrieveDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        # token = Token.objects.create(user=user)
        return Response({'user': serializer.data})
    return Response(serializer.errors, status=status.HTTP_200_OK)

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    # token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'user': serializer.data})