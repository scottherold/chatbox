from django.db import models
from ..users.models import User

# Create your models here.
class FriendManager(models.Manager):
    def add_friend(self, form):        
        friend_user = User.objects.get(id=form['friend_user_id'])
        friend_from = User.objects.get(id=form['user_id'])  
             
        try:
            
            add_friend = self.get(friend_from=friend_from, friend_user=friend_user)
            print("Already friend with this user")
        except:
            self.create(friend_from=friend_from, friend_user=friend_user)
            print("i am the user",friend_from.first_name,"and i friended " ,friend_user.first_name) 

    def delete_friend(self,form):
        friend_user = User.objects.get(id=form['friend_user_id'])
        friend_from = User.objects.get(id=form['user_id'])
        self.get(friend_from=friend_from, friend_user=friend_user).delete()
        
        try:
            self.get(friend_from=friend_user, friend_user=friend_from).delete()
        except:
            pass
        print("You unfriended ",friend_user.first_name, "<<<<<-------" )



class Friend(models.Model):
    friend_from = models.ForeignKey(User, related_name="friended_from_user") #person who made the friend request
    friend_user = models.ForeignKey(User, related_name="friend_user") #person who received the friend request
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = FriendManager()