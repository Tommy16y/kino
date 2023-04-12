# Generated by Django 4.2 on 2023-04-12 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='films')),
                ('title', models.CharField(max_length=255)),
                ('tags', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('description', models.TextField()),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
    ]