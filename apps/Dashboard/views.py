from django.shortcuts import render,redirect
from ..message .models import Post
from ..users.models import User
from ..pokes.models import Poke
# Create your views here.


def homePage(req):

    if 'user_id' not in req.session:
        return redirect("users:registration")

    context={
        'posts':Post.objects.all(),
    }
    return render(req,"dashboard/homePage.html",context)


def profile(req,user_id):

    poke_list = Poke.objects.filter(poke_user__id=user_id)

    context={
        'user': User.objects.get(id=user_id),
        'poke_list': poke_list,
        'poke_count': poke_list.count()
    }
    return render(req,"dashboard/profilePage.html",context)


def find_friends(req):
    
    context={
        'users':User.objects.all()
    }
    return render(req, "dashboard/find_friends.html",context)