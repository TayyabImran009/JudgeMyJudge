from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from registration.models import UserProfile
from registration.forms import*
from django.contrib.auth import authenticate

# Create your views here.


@login_required(login_url="loginPage")
def profile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    print(profile)
    context = {'profile': profile}

    if request.method == 'POST':
        user.first_name = request.POST['first_name']
        user.email = request.POST['email']
        user.username = request.POST['username']
        user.save()

        profile.date_of_birth = request.POST['date_of_birth']
        profile.address = request.POST['address']
        profile.case_number = request.POST['case_number']
        if request.FILES.get('picture_id'):
            profile.picture_id = request.FILES['picture_id']
        profile.save()

        return redirect('profile')

    return render(request, 'person/profile.html', context)


@login_required(login_url="loginPage")
def changePassword(request):
    if request.method == 'POST':
        u = request.user
        print(u.password)
        if authenticate(request, username=u.username,
                        password=request.POST['currentPassword']):
            u.set_password(request.POST['newpassword1'])
            u.save()
            print(u.password)
            return redirect('logout')

    return redirect('profile')


def home(request):
    return render(request, 'home.html')
