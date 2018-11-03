from django.shortcuts import render,redirect
from ..message .models import Post
from ..users.models import User
# Create your views here.


def homePage(req):

    if 'user_id' not in req.session:
        return redirect("users:registration")

    context={
        'posts':Post.objects.all()
    }

    return render(req,"dashboard/homePage.html",context)


def profile(req,user_id):


    context={
        'user': User.objects.get(id=user_id)
    }
    return render(req,"dashboard/profilePage.html",context)



