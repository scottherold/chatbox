from django.shortcuts import render, redirect
from django.contrib import messages
from ..pokes.models import Poke
from .models import User
# Create your views here.

def index(req):
    if 'user_id' in req.session:
        return redirect('users:pokes')
    else:
        return redirect('users:main')

def create(req):
    if req.method != 'POST':
        return redirect('users:main')
    errors = User.objects.validate(req.POST)
    if len(errors) > 0:
        for error in errors:
            messages.error(req, error)
    else:
        user = User.objects.create_user(req.POST)
        req.session['user_id'] = user.id
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

def login(req):
    if req.method != 'POST':
        return redirect('users:main')
    valid, response = User.objects.login(req.POST)
    if valid == True:
        req.session['user_id'] = response
        return redirect("users:index")
    else:
        messages.error(req, response)
    return redirect('users:index')

def logout(req):
    req.session.clear()
    return redirect("users:index")

def main(req):
    return render(req, 'users/main.html')

def pokes(req):
    user = User.objects.get(id=req.session['user_id'])
    poke_list = Poke.objects.filter(poke_user__id=req.session['user_id']).order_by("-poke_count")
    context = {
        'user': user,
        'user_list': User.objects.all().exclude(id=user.id),
        'poke_list': poke_list,
        'poke_count': poke_list.count()
    }
    print(context['poke_list'].values())
    return render(req, 'users/index.html', context)