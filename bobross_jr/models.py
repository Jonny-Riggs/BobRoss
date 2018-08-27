from django.db import models

# Create your models here.
# TODO: Make a Birthday models

# date:
# name:
# greeting

# makemigrations
# migrate
# in DB Browser add three birthday instances

# make a url conf
# make a view for sending back birthday data

class Birthday(models.Model):
    name = models.CharField(max_length=20)
    greeting = models.TextField()
    date = models.DateField()