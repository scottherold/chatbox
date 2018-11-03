from django.shortcuts import render, redirect
from django.contrib import messages
from ..pokes.models import Poke
from .models import User
# Create your views here.

def home(req):

    return render(req,'users/home.html')

def register(req):
     
    return render(req,'users/register.html')

    
def create(req):

    if req.method != 'POST':
        return redirect('users:main')

    errors = User.objects.validate(req.POST)

    req.session['tempUserData']={
        'firstname':req.POST['first_name'],
        'lastname':req.POST['last_name'],
        'username':req.POST['user_name'],
        'email':req.POST['email']
    }
    if len(errors) > 0:
        for error in errors:
            req.session['messageColor']="danger"
            messages.error(req, error)
    else:
        user = User.objects.create_user(req.POST)

        # delete the temporary user data
        del req.session['tempUserData']

        req.session['user_id'] = user.id

        req.session['messageColor']="success"
        messages.success(req, "Successfully Registered")
        return redirect('dashboard:homePage')

    return redirect('users:registration')
    

def update(req, user_id):

    errors=User.objects.EditUser(req.POST,req.session["user_id"])

    if len(errors) > 0:
        for error in errors:
            req.session['messageColor']="danger"
            messages.error(req, error)
    else:

        req.session['messageColor']="success"
        messages.success(req, "Update Successfully")

    return redirect('dashboard:profile',user_id=user_id )


def login(req):

    return render(req,'users/login.html')
    
def LoginProccess(req):

    if req.method != 'POST':
        return redirect('users:registration')

    valid,response=User.objects.login(req.POST)

    if valid == True:
        req.session['user_id'] = response
        # color of message
        req.session['messageColor']="success"
        messages.success(req, "Successfully Log In")

        return redirect("dashboard:homePage")
    else:
        for error in response:
            req.session['messageColor']="danger"
            messages.error(req, error)
    return redirect('users:login')


def logout(req):
    req.session.clear()
    return redirect('users:login')





def destroy(req, id):
    pass

def new(req):
    pass

def edit(req, id):
    pass

def show(req, id):
    pass