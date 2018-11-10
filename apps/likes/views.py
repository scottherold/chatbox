from django.shortcuts import render, redirect,HttpResponse
from django.http import JsonResponse
from.models import Like_Comment,Like_Post
from ..users.models import User
from ..message.models import Post,Comment
# Create your views here.

def like_Post(req,post_id,location):

    didUserLiked= Like_Post.objects.filter(postLiked_id=post_id).filter(userWhoLiked_id=req.session['user_id'])

    if didUserLiked:
        print("The user cannot like this Post<<<<<<<-----")
       
    else:
        print("the user can like the Post<<<<<<------")
        Like_Post.objects.create(
            userWhoLiked=User.objects.get(id=req.session['user_id']),
            postLiked=Post.objects.get(id=post_id))
    
    # That's for ajax like feature
    # total_likes=Post.objects.get(id=post_id).likePost.all().count()
    # return JsonResponse({'total_likes': total_likes})

    if location=="profile":
        return redirect("dashboard:profile", user_id=req.session['user_id'])
    elif location=="homePage":
        return redirect("dashboard:homePage")

def like_Comment(req,comment_id,location):

    didUserLiked= Like_Comment.objects.filter(commentLiked_id=comment_id).filter(userWhoLiked_id=req.session['user_id'])

    if didUserLiked:
        print("The user cannot like this Post<<<<<<<-----")
    else:
        print("the user can like the Post<<<<<<------")
        Like_Comment.objects.create(
            userWhoLiked=User.objects.get(id=req.session['user_id']),
            commentLiked=Comment.objects.get(id=comment_id))

    if location=="profile":
        return redirect("dashboard:profile", user_id=req.session['user_id'])
    elif location=="homePage":
        return redirect("dashboard:homePage")

def index(req):
    pass

def create(req):
    pass

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