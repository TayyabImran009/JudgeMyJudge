from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, UserProfileForm


# Create your views here.


def loginPage(request):

    page = "login"

    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User not recognized.')

        user = authenticate(request, username=username,
                            password=password)  # check password

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Username or Password is invalid')

    context = {'page': page}
    return render(request, 'registration/login_signup_form.html', context)


def registerUser(request):
    form = CustomUserCreationForm
    profile_form = UserProfileForm()
    page = "register"
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            messages.success(request, 'Account is Created')

            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "An error occured")
    context = {'page': page, 'form': form, 'profile_form': profile_form}
    return render(request, 'registration/login_signup_form.html', context)


def logoutUser(request):
    logout(request)
    messages.info(request, "User loged out!")
    return redirect('loginPage')


def home(request):
    return render(request, 'home.html')
