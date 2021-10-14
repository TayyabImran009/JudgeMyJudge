from django.shortcuts import render, redirect
import csv
from .models import judge
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import*
from registration.models import UserProfile
# Create your views here.


def loadData(request):
    with open('data.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            judge.objects.create(location=row[0], general_district_court=row[1], position1=row[2],
                                 juvenile_domestic_court=row[3], position2=row[4], circuit_court=row[5], position3=row[6])
    return render(request, 'home.html')


@login_required(login_url="loginPage")
def autocomplete(request):
    if 'term' in request.GET:
        judgeList = judge.objects.filter(
            location__istartswith=request.GET.get('term'))
        searchJudge = list()
        for j in judgeList:
            searchJudge.append(j.location)
        return JsonResponse(searchJudge, safe=False)


@login_required(login_url="loginPage")
def getJudge(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        try:
            judgeInfo = judge.objects.get(location=search_query)
            print(judgeInfo)
            context = {'judgeInfo': judgeInfo, 'profile': profile}
            return render(request, 'judge/ratejudge.html', context)
        except User.DoesNotExist:
            owner = None
    else:
        return redirect('profile')
