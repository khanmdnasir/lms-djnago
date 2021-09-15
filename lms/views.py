from lms.forms import UserForm, UserProfileForm
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'lms/home.html')

def register(request):
    registered=False
    if request.method == "POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()

            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileForm()
    return render(request,'lms/registration.html',{'registered':registered,'user_form':user_form,'profile_form':profile_form})

def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Account is deactivated")
        else:
            return HttpResponse("please use correct id and password")
    else:
        return render(request,'lms/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))