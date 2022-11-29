from django.shortcuts import redirect, render
from .models import Account
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User


# Create your views here.
def login_s(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

        else:
            return redirect('/login/')
    else:
        return render(request, "page-user-login.html")

    return redirect('home')


def register(request):
    if request.method == "POST":
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        country = request.POST['country']
        city = request.POST['city']
        gender = request.POST['gender']
        password = request.POST['password']
        username = request.POST['username']

        user = User.objects.create_user(username=username, email=email, password=password)
        Account.objects.create(user=user, first_name=first_name, last_name=last_name, gender=gender, country=country, city=city)
        a = authenticate(username=first_name, password=password)
        login(request, a)
    else:
        return render(request, "page-user-register.html")

    return redirect('home')




def profile(request):
    if request.user.is_authenticated:
        data = {
            "user": Account.objects.get(user=request.user),
        }
        return render(request, "page-profile-main.html", data)
    return redirect('/login/')

def address(request):
    if request.user.is_authenticated:
        return render(request, "page-profile-address.html")
    return redirect('/login/')

def order(request):
    if request.user.is_authenticated:
        return render(request, "page-profile-orders.html")
    return redirect('/login/')

def wishlist(request):
    if request.user.is_authenticated:
        return render(request, "page-profile-wishlist.html")
    return redirect('/login/')

def setting(request):
    if request.user.is_authenticated:
        data = {
           "user": Account.objects.get(user=request.user),
        }
        return render(request, "page-profile-setting.html", data)
    return redirect('/login/')

def selling(request):
    if request.user.is_authenticated:
        return render(request, "page-profile-seller.html")
    return redirect('/login/')

def logout_a(request):
    logout(request)
    return redirect('/login/')