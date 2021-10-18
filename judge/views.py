from django.forms.widgets import HiddenInput
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
            if row[1] != "":
                judge.objects.create(location=row[0], name=row[1], position=row[2],
                                     coat_name=row[3])
    return render(request, 'home.html')


def removeSpace(request):
    jd = judge.objects.all()
    for j in jd:
        j.location = j.location.rstrip()
        j.save()
    return render(request, 'home.html')


def autocomplete(request):
    if 'term' in request.GET:
        judgeList = judge.objects.filter(
            name__istartswith=request.GET.get('term'))
        searchJudge = list()
        for j in judgeList:
            searchJudge.append(j.name + ", " + j.location)
        return JsonResponse(searchJudge, safe=False)


def getJudge(request):
    profile = ""
    user = request.user
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=user)
    search_query = ''
    total_rating = 0
    if request.GET.get('search_query'):
        s_query = request.GET.get('search_query')
        s_query = s_query.split(',')
        if s_query[0]:
            j_name = s_query[0]
        if s_query[1]:
            j_location = s_query[1].replace(" ", "")
        try:
            judgeInfo = judge.objects.get(
                name=j_name, location=j_location)
            try:
                ratting = judgeRateing.objects.filter(ratedTo=judgeInfo)
                total_num = (len(ratting))*5
                obtain_num = 0
                for r in ratting:
                    obtain_num += r.rating
                if total_num != 0:
                    total_rating = (obtain_num/total_num)*5

            except User.DoesNotExist:
                ratting = ''

            context = {'judgeInfo': judgeInfo,
                       'profile': profile, 'ratting': ratting, 'total_rating': total_rating}
            return render(request, 'judge/ratejudge.html', context)
        except User.DoesNotExist:
            judgeInfo = ""
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
        total_num = (len(ratting))*5
        obtain_num = 0
        for r in ratting:
            obtain_num += r.rating
        if total_num != 0:
            total_rating = (obtain_num/total_num)*5
        context = {'judgeInfo': judgeInfo,
                   'profile': profile, 'ratting': ratting, 'total_rating': total_rating}
        return render(request, 'judge/ratejudge.html', context)
    else:
        judgeInfo = judge.objects.get(id=pk)
        profile = UserProfile.objects.get(user=request.user)
        ratting = judgeRateing.objects.filter(ratedTo=judgeInfo)
        profile = UserProfile.objects.get(user=request.user)
        ratting = judgeRateing.objects.filter(ratedTo=judgeInfo)
        total_num = (len(ratting))*5
        obtain_num = 0
        for r in ratting:
            obtain_num += r.rating
        if total_num != 0:
            total_rating = (obtain_num/total_num)*5
        context = {'judgeInfo': judgeInfo,
                   'profile': profile, 'ratting': ratting, 'total_rating': total_rating}
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
