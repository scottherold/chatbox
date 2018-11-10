from django.shortcuts import render,redirect

# Create your views here.
def pacman(request):
    return render(request,"game/pacman.html")


def Airforce(request):
    return render(request,"game/1942Battle.html")


def gameScore(request):
    print(request.POST['scores'])
    return redirect ("dashboard:homePage")