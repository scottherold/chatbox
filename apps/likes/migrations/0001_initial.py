# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-05 14:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like_Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('commentLiked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likeComment', to='message.Comment')),
                ('userWhoLiked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_ReplyUser', to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='Like_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('postLiked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likePost', to='message.Post')),
                ('userWhoLiked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_PostUser', to='users.User')),
            ],
        ),
    ]