from django.shortcuts import render, redirect
from .models import Friend

# Create your views here.

# def index(req):
#     pass

def create(req,user_id):
    Friend.objects.add_friend(req.POST)

    if req.POST["location"]=="find_friend":
        return redirect('dashboard:find_friends')
    elif req.POST["location"]=="profilePage":
        return redirect('dashboard:profile',user_id=user_id)

def delete(req, user_id):

    Friend.objects.delete_friend(req.POST)
    return redirect('dashboard:profile',user_id=user_id)


def new(req):
    pass

def edit(req, id):
    pass

def show(req, id):
    pass