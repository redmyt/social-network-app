from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField()

    def __str__(self):
        return self.user.username


class Message(models.Model):
    sender = models.ForeignKey(Profile,
                                on_delete=models.CASCADE,
                                related_name='sender')

    receiver = models.ForeignKey(Profile,
                                on_delete=models.CASCADE,
                                related_name='receiver')

    message_body = models.TextField(blank=False)
    date = models.DateField()


class FriendsRecord(models.Model):
    first_friend = models.ForeignKey(Profile,
                                    on_delete=models.CASCADE,
                                    related_name='first_friend')

    second_friend = models.ForeignKey(Profile,
                                    on_delete=models.CASCADE,
                                    related_name='second_friend')
