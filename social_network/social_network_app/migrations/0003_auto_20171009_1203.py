# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 12:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_network_app', '0002_auto_20171004_1615'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='Profile',
        ),
    ]