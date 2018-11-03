from django.db import models
from ..users.models import User
# Create your models here.
class PostManager(models.Manager):
    def post_validation(self,form,user_id):
        errors=[]
        if len(form['post'])<1:
            errors.append("Post cannot be blank")
        if len(form['post'])>240:
            errors.append("Post content exceeded the maximum limit which is 240 characters")

        if errors:
            return(errors)
        else:
            Post.objects.create(
                content=form['post'],
                user=User.objects.get(id=user_id)
            )
            return(errors)

    def Comment_validation(self,form,user_id,post_id):
        errors=[]
        if len(form['comment'])<1:
            errors.append("comment cannot be blank")
        if len(form['comment'])>150:
            errors.append("comment content exceeded the maximum limit which is 150 characters")

        if errors:
            return(errors)
        else:
            Comment.objects.create(
                content=form['comment'],
                user=User.objects.get(id=user_id),
                post=Post.objects.get(id=post_id)
            )

            return(errors)


    def Reply_validation(self,form,user_id,comment_id):
        errors=[]
        print(comment_id)
        if len(form['reply'])<1:
            errors.append("reply cannot be blank")
        if len(form['reply'])>100:
            errors.append("reply content exceeded the maximum limit which is 100 characters")

        if errors:
            return(errors)
        else:
            Reply.objects.create(
                content=form['reply'],
                belongTo=int(form['reply_id']),
                user=User.objects.get(id=user_id),
                comment=Comment.objects.get(id=comment_id)
            )

            return(errors)


class Post(models.Model):
    content=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user=models.ForeignKey(User,related_name='post')
    objects = PostManager()

class Comment(models.Model):
    content=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    post=models.ForeignKey(Post,related_name='comment')
    user=models.ForeignKey(User,related_name='commentedUser')
    objects = PostManager()

class Reply(models.Model):
    content=models.TextField()
    belongTo=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    comment=models.ForeignKey(Comment,related_name='reply')
    user=models.ForeignKey(User,related_name='repliedUser')
    objects = PostManager()