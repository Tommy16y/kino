from django.shortcuts import render
from django.contrib.auth import get_user_model  
from .serializer import RegisterSerializer,ChangePasswordSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from django.contrib.auth.hashers import check_password
from rest_framework import generics, status

User = get_user_model()


class RegisterAPIView(APIView):
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response('Вы успешно зарегистрировались', status=201)
    
class LogoutAPIView(APIView):
    permission_classes =[IsAuthenticated]
    def post(self,request):
        try:
            user = request.user
            Token.objects.get(user=user).delete()
            return Response('Вы успешно разлогинились',status=200)
        except:
            return Response(status=403)
        
    

# class ChangePasswordView(generics.UpdateAPIView):
  
#     model = User
#     serializer_class = ChangePasswordSerializer
    
#     def get_object(self, queryset=None):
#         return self.request.user

#     def update(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         serializer = self.get_serializer(data=request.data)

#         if serializer.is_valid():
#             self.object.set_password(serializer.data.get("new_password"))
#             self.object.save()
            
#             return Response('Пароль успешно изменен', status=status.HTTP_200_OK)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(APIView):
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            login = serializer.validated_data['login']
            new_password = serializer.validated_data['new_password']
            user = User.objects.get(login=login)
            user.set_password(new_password)
            user.save()
            return Response('Пароль успешно изменен', status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
