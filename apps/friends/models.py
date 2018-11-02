from django.db import models
from ..users.models import User

# Create your models here.
class FriendManager(models.Manager):
    def add_friend(self, form):        
        friend_user = User.objects.get(id=form['friend_user_id'])
        friend_from = User.objects.get(id=form['user_id'])        
        try:
            add_friend = self.get(friend_from=friend_from, friend_user=friend_user)
        except:
            self.create(friend_from=friend_from, friend_user=friend_user)

class Friend(models.Model):
    friend_from = models.ForeignKey(User, related_name="friended_from_user")
    friend_user = models.ForeignKey(User, related_name="friend_user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = FriendManager()