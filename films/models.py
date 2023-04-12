from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Film(models.Model):
    image = models.ImageField(upload_to='films')
    title = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    year = models.IntegerField()
    description = models.TextField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}'

User =get_user_model()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user.username} - {self.film.title}'