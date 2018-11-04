from django.shortcuts import render,redirect
from ..message .models import Post
from ..users.models import User
from ..pokes.models import Poke
from ..friends.models import Friend
# Create your views here.


def homePage(req):

    if 'user_id' not in req.session:
        return redirect("users:registration")

    context={
        'posts':Post.objects.all().order_by("-created_at"),
        'friends':User.objects.filter(friended_from_user__friend_user=req.session['user_id']).filter(friend_user__friend_from=req.session['user_id'])
    }
    return render(req,"dashboard/homePage.html",context)


def profile(req,user_id):

    poke_list = Poke.objects.filter(poke_user__id=user_id)
    friend_list=Friend.objects.filter(friend_user_id=user_id)
    Are_you_Friend=False
    waitingForConfirmation=True
    if int(user_id) != req.session['user_id']:

        # checking if they are friends and still waiting for confirmation.....
        try:
            Friend.objects.get(friend_from=req.session['user_id'], friend_user=user_id)
            waitingForConfirmation=True

            try:
                Friend.objects.get(friend_from=user_id,friend_user=req.session['user_id'])
                Are_you_Friend=True
            except:
                Are_you_Friend=False

        except:
            waitingForConfirmation=False
            print("Not friends")
    
    context={
        'user': User.objects.get(id=user_id),
        'friends':User.objects.filter(friended_from_user__friend_user=user_id).filter(friend_user__friend_from=user_id),
        'poke_list': poke_list,
        'poke_count': poke_list.count(),
        'totalFriend': friend_list.count(),
        'waitingForConfirmation':waitingForConfirmation,
        'Are_you_Friend':Are_you_Friend
    }
    return render(req,"dashboard/profilePage.html",context)


def find_friends(req):
    # Friend.objects.filter(friend_user_id=req.session['user_id']).exclude(friend_from_id=req.session['user_id'])
    # User.objects.exclude(friend_user__friend_from=req.session['user_id']).exclude(friend_user=req.session['user_id'])
    context={
        'friend_request':User.objects.filter(friended_from_user__friend_user=req.session['user_id']).exclude(friend_user__friend_from=req.session['user_id']),
        'potentialFriends':User.objects.exclude(friend_user__friend_from=req.session['user_id']).exclude(id=req.session['user_id'])
    }
    
    return render(req, "dashboard/find_friends.html",context)