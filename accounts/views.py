from django.shortcuts import render, redirect, reverse
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from .forms import RegistrationUserForm, UserLoginForm


def register(request):
    context = {}
    if request.POST:
        form = RegistrationUserForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Registration successful!')

            return redirect('accounts:login')
        context['form'] = form
    else:
        form = RegistrationUserForm()
        context['form'] = form
    return render(request, 'accounts/register.html', context)


def login_page(request):
    context = {}
    if request.POST:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('portal:portal')
        else:
            context['login_form'] = form

    else:
        form = UserLoginForm()
        context['login_form'] = form

    return render(request, 'accounts/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('accounts:login')


def forgot_password(request):
    # form = UserCreationForm()
    # context = {"form": form}
    return render(request, 'accounts/forgotpassword.html')
