# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-04 18:40
from __future__ import unicode_literals

from django.db import migrations
from pulseapi import users, profiles


def copy_bookmarks_from_user_to_prolfies(apps, schema_editor):
    EmailUser = apps.get_model('users', 'EmailUser')
    ProfileUserBookmarks = apps.get_model('profiles', 'UserBookmarks')
    UserProfile = apps.get_model('profiles', 'UserProfile')

    current_bookmarks = apps.get_model('users', 'UserBookmarks').objects.all()
    for bookmark in current_bookmarks:
        user = EmailUser.objects.get(id=bookmark.user.id)
        profile = UserProfile.objects.get(user=user)

        (nbm, created) = ProfileUserBookmarks.objects.get_or_create(
            user=user,
            profile=profile,
            entry=bookmark.entry,
            timestamp=bookmark.timestamp
        )

        if created is True:
            msg = "created a parallel bookmark between user:{u} and entry:{e}"
            msg = msg.format(u=user.id, e=bookmark.entry.id)
            print(msg)


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_userbookmarks_profile'),
        ('users', '0004_auto_20170616_1131'),
    ]

    operations = [
        migrations.RunPython(copy_bookmarks_from_user_to_prolfies),
    ]
