from django.shortcuts import render, redirect
from .models import Friend

# Create your views here.

# def index(req):
#     pass

def create(req):
    Friend.objects.add_friend(req.POST)
    return redirect('users:index')

def update(req, id):
    pass

def destroy(req, id):
    pass

def new(req):
    pass

def edit(req, id):
    pass

def show(req, id):
    pass