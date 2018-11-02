from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post,Comment,Reply
# Create your views here.
print("Checking my pull request and Forking")




def createPost(request):

    errors=Post.objects.post_validation(request.POST,request.session['user_id'])

    if errors==True:
        for error in errors:
            request.session['messageColor']="danger"
            messages.error(request, error)
    else:
        request.session['messageColor']="success"
        messages.success(request, "Post Successfully Created")
    
    return redirect('dashboard:homePage')



def createComment(request,post_id):

    errors=Comment.objects.Comment_validation(request.POST,request.session['user_id'],post_id)

    if errors==True:
        for error in errors:
            request.session['messageColor']="danger"
            messages.error(request, error)
    
    return redirect('dashboard:homePage')



def createReply(request,comment_id):
    print(request.POST)
    errors=Reply.objects.Reply_validation(request.POST,request.session['user_id'],comment_id)
    
    if errors==True:
        for error in errors:
            request.session['messageColor']="danger"
            messages.error(request, error)
    
    return redirect('dashboard:homePage')



def delete(request,post_id):
    try:
        Post.objects.get(id=post_id).delete()
    except:
        request.session['messageColor']="danger"
        messages.error(request, "Unable to delete your Post. Pease contact our nearby office for assistance")

    return redirect('dashboard:homePage')