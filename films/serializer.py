from .models import Film,Like
from rest_framework import serializers
from django.contrib.auth import get_user_model


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'image', 'title', 'tags', 'year', 'description', 'likes')

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