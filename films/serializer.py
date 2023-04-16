from .models import Film,Like, Tag,Genre
from rest_framework import serializers
from django.contrib.auth import get_user_model
import django_filters


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'image', 'title', 'tags', 'year', 'description', 'likes','genre')

    def get_likes(self, obj):
        return obj.likes.filter(user=self.context['request'].user).exists()
    
    def create(self, validated_data):
        film = Film.objects.create(**validated_data)
        film.likes.create(user=self.context['request'].user)
        return film
    
    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.title = validated_data.get('title', instance.title)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.year = validated_data.get('year', instance.year)
        instance.genre = validated_data.get('genre',instance.genres)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
    


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['film', 'user']

    def validate(self, attrs):
        film = attrs['film']
        user = attrs['user']
        if Like.objects.filter(film=film, user=user).exists():
            raise serializers.ValidationError("Вы уже поставили лайк на этот фильм")
        return attrs
    



class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['name']




class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['name']




class GenreFilter(django_filters.FilterSet):
    genre = django_filters.CharFilter(field_name='genres__name')

    class Meta:
        model = Film
        fields = ['genre']


class TagsFilter(django_filters.FilterSet):
    tags = django_filters.CharFilter(field_name='tags__name')

    class Meta:
        model = Film
        fields = ['tags']


class YearFilter(django_filters.FilterSet):
    year = django_filters.CharFilter(field_name='year__name')

    class Meta:
        model = Film
        fields = ['year']