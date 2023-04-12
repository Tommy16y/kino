from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Film,Like
from .serializer import FilmSerializer,LikeSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes

class FilmListCreateView(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = (IsAdminUser,)

class FilmDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = (IsAdminUser,)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_like(request, film_id):
    
    user = request.user
    try:
        like = Like.objects.get(user=user, film=film_id)
        like.delete()
        film = Film.objects.get(id=film_id)
        film.likes -= 1
        film.save()
        message = "Лайк удален"
    except Like.DoesNotExist:
        like = Like(user=user, film_id=film_id)
        like.save()
        film = Film.objects.get(id=film_id)
        film.likes += 1
        film.save()
        message = "Лайк поставлен"
    serializer = LikeSerializer(like)
    return Response({'message': message}, status=status.HTTP_200_OK)
