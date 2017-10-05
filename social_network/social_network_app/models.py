from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user')
    phone = models.IntegerField()

    def __str__(self):
        return self.user.username


class Message(models.Model):
    sender = models.ForeignKey(UserProfile,
                                on_delete=models.CASCADE,
                                related_name='sender')

    receiver = models.ForeignKey(UserProfile,
                                on_delete=models.CASCADE,
                                related_name='receiver')

    message_body = models.TextField(blank=False)
    date = models.DateField()


class FriendsRecord(models.Model):
    first_friend = models.ForeignKey(UserProfile,
                                    on_delete=models.CASCADE,
                                    related_name='first_friend')

    second_friend = models.ForeignKey(UserProfile,
                                    on_delete=models.CASCADE,
                                    related_name='second_friend')
