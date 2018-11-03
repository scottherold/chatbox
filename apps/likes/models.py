from django.db import models
from..users.models import User
from ..message.models import Post,Comment
# Create your models here.

class Like_Post(models.Model):
    userWhoLiked=models.ForeignKey(User,related_name='liked_PostUser')
    postLiked=models.ForeignKey(Post,related_name='likePost')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Like_Comment(models.Model):
    userWhoLiked=models.ForeignKey(User,related_name='liked_ReplyUser')
    commentLiked=models.ForeignKey(Comment,related_name='likeComment')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)