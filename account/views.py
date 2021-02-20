from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CreateUserForm,ProfileUpdateForm,UserUpdateForm
from django.contrib import messages
from home import urls
from . import urls

# Create your views here.
def register(request):
    if  request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        phone = request.POST.get('phone')
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        if password == confirmpassword :
            register_user = User.objects.create_user(username = user_name, password = password, email = email, first_name = first_name, last_name = last_name, Pzzhone = phone)

            register_user.save()
            return redirect('form')
        else:
            messages.error(request, 'ERROR: THE TWO PASSWORDS DOES NOT MATCH !!!')
            return render(request, "pages/register.html")
    
    else:
        return render(request, "pages/register.html")



def form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'ERROR: INCORRECT USER OR PASSWORD !!!')
            return redirect('form')  

    else:
         return render(request, "pages/form.html")



def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('form')  

@login_required
def profile(request):
    # if request.method == 'POST':
    #     userUpdateForm = UserUpdateForm(request.POST, instance = request.user)
    #     profileUpdateForm = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
    # else:
    #     userUpdateForm = UserUpdateForm(instance = request.user)
    #     profileUpdateForm = ProfileUpdateForm(instance = request.user.profile)    
    #     #saving the forms

    # if userUpdateForm.is_valid() and profileUpdateForm.is_valid():
    #     userUpdateFormform.save()
    #     profileUpdateForm.save()

    #     return redirect('login')

    #     context = {
    #         'userUpdateForm': userUpdateForm,
    #         'profileUpdateForm': profileUpdateForm
    #     }    

    #this page is to show only when the user is successfully logged in
    return render(request,'pages/profile.html')         
               