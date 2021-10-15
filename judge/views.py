from django.shortcuts import render, redirect
import csv
from .models import judge
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import*
from registration.models import UserProfile
from .forms import bestInterestForm
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

            try:
                ratting = judgeRateing.objects.filter(ratedTo=judgeInfo)
            except User.DoesNotExist:
                ratting = ''

            context = {'judgeInfo': judgeInfo,
                       'profile': profile, 'ratting': ratting}
            return render(request, 'judge/ratejudge.html', context)
        except User.DoesNotExist:
            owner = None
    else:
        return redirect('profile')


def rateJudge(request, pk):
    if request.method == 'POST':
        user = request.user
        ratedTo = judge.objects.get(id=request.POST['judge_id'])
        rating = int(request.POST['score'])
        description = request.POST['description']
        cannon1 = request.POST['cannon1']
        cannon2 = request.POST['cannon2']
        cannon3 = request.POST['cannon3']
        cannon4 = request.POST['cannon4']
        cannon5 = request.POST['cannon5']
        political_perspective_of_judge = request.POST['political_perspective_of_judge']
        family_connections_in_legal_community = request.POST['family_connections_in_legal_community']

        r = judgeRateing(user=user, ratedTo=ratedTo, rating=rating, description=description,
                         cannon1=cannon1, cannon2=cannon2, cannon3=cannon3, cannon4=cannon4, cannon5=cannon5, political_perspective_of_judge=political_perspective_of_judge, family_connections_in_legal_community=family_connections_in_legal_community)
        r.save()
        judgeInfo = judge.objects.get(id=request.POST['judge_id'])
        profile = UserProfile.objects.get(user=request.user)
        ratting = judgeRateing.objects.filter(ratedTo=judgeInfo)
        context = {'judgeInfo': judgeInfo,
                   'profile': profile, 'ratting': ratting}
        return render(request, 'judge/ratejudge.html', context)
    else:
        judgeInfo = judge.objects.get(id=pk)
        profile = UserProfile.objects.get(user=request.user)
        ratting = judgeRateing.objects.filter(ratedTo=judgeInfo)
        context = {'judgeInfo': judgeInfo,
                   'profile': profile, 'ratting': ratting}
        return render(request, 'judge/ratejudge.html', context)


def bestIntrest(request, pk):
    if request.method == 'POST':
        form = bestInterestForm(request.POST)
        if form.is_valid():
            bestInt = form.save(commit=False)
            bestInt.user = request.user
            bestInt.ratedTo = judge.objects.get(id=pk)
            bestInt.save()
            judgeInfo = judge.objects.get(id=pk)
            profile = UserProfile.objects.get(user=request.user)
            ratting = judgeRateing.objects.filter(ratedTo=judgeInfo)
            context = {'judgeInfo': judgeInfo,
                       'profile': profile, 'ratting': ratting}
            return render(request, 'judge/ratejudge.html', context)
    else:
        judgeInfo = judge.objects.get(id=pk)
        profile = UserProfile.objects.get(user=request.user)
        ratting = judgeRateing.objects.filter(ratedTo=judgeInfo)
        context = {'judgeInfo': judgeInfo,
                   'profile': profile, 'ratting': ratting}
        return render(request, 'judge/ratejudge.html', context)
