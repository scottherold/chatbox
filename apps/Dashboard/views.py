from django.shortcuts import render,redirect

# Create your views here.


def homePage(req):

    if 'user_id' not in req.session:
        return redirect("users:registration")



    return render(req,"dashboard/homePage.html")


def profile(req,user_id):


    context={
        'user_id':user_id
    }
    return render(req,"dashboard/profilePage.html",context)