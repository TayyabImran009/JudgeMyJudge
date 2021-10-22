from django.forms.widgets import HiddenInput
from django.shortcuts import render, redirect
import csv
from .models import judge
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import*
from registration.models import UserProfile
from .forms import bestInterestForm, judgeRateingForm
from django.views.decorators.csrf import csrf_exempt
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


def autocompleteLocation(request):
    if 'term' in request.GET:
        judgeList = judge.objects.filter(
            location__istartswith=request.GET.get('term'))
        searchJudge = list()
        for j in judgeList:
            if j.location not in searchJudge:
                searchJudge.append(j.location)
        return JsonResponse(searchJudge, safe=False)


def autocomplete2(request, pk):
    j = judge.objects.filter(
        name__istartswith=pk).values()
    jugeslist = list(j)

    return JsonResponse({'jugeslist': jugeslist})


def autocomplete3(request, pk):
    judgesList = judge.objects.filter(
        location__istartswith=pk)
    locationlist = list()
    for l in judgesList:
        if l.location not in locationlist:
            locationlist.append(l.location)
    return JsonResponse({'locationlist': locationlist})


def getJudgeByLocation(request, name):
    judgeList = judge.objects.filter(location=name)
    location = judgeList[0].location
    context = {'judgeList': judgeList, 'location': location}
    return render(request, 'judge/judgesByLocation.html', context)


def getJudge(request):
    profile = ""
    user = request.user
    canrate = True
    canbestintrest = True
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
                    if r.user == request.user:
                        canrate = False
                if total_num != 0:
                    total_rating = (obtain_num/total_num)*5

            except User.DoesNotExist:
                ratting = ''

            try:
                bestIntrest = bestInterest.objects.filter(ratedTo=judgeInfo)
                for r in bestIntrest:
                    if r.user == request.user:
                        canbestintrest = False

            except User.DoesNotExist:
                bestIntrest = ''
            context = {'judgeInfo': judgeInfo,
                       'profile': profile, 'ratting': ratting, 'total_rating': total_rating, 'canrate': canrate, 'canbestintrest': canbestintrest}
            return render(request, 'judge/ratejudge.html', context)
        except User.DoesNotExist:
            judgeInfo = ""
    else:
        return redirect('profile')


def rateJudge(request, pk):
    canrate = True
    canbestintrest = True
    user = request.user
    ratedTo = judge.objects.get(id=pk)
    ratting = judgeRateing.objects.filter(ratedTo=ratedTo)
    if request.method == 'POST':
        rating = int(request.POST['score'])
        description = request.POST['description']
        cannon1 = request.POST['cannon1']
        cannon2 = request.POST['cannon2']
        cannon3 = request.POST['cannon3']
        cannon4 = request.POST['cannon4']
        cannon5 = request.POST['cannon5']
        political_perspective_of_judge = request.POST['political_perspective_of_judge']
        family_connections_in_legal_community = request.POST['family_connections_in_legal_community']

        ratedTo.numberOfRatings += 1
        ratedTo.obtainScore += rating
        ratedTo.save()

        r = judgeRateing(user=user, ratedTo=ratedTo, rating=rating, description=description,
                         cannon1=cannon1, cannon2=cannon2, cannon3=cannon3, cannon4=cannon4, cannon5=cannon5, political_perspective_of_judge=political_perspective_of_judge, family_connections_in_legal_community=family_connections_in_legal_community)
        r.save()

        updateRatting(pk)

        ratedTo = judge.objects.get(id=pk)
        ratting = judgeRateing.objects.filter(ratedTo=ratedTo)

        try:
            bestIntrest = bestInterest.objects.filter(ratedTo=pk)
            for b in bestIntrest:
                if b.user == request.user:
                    canbestintrest = False
        except User.DoesNotExist:
            bestIntrest = ''

        for r in ratting:
            if r.user == request.user:
                canrate = False

        context = {'judgeInfo': ratedTo,
                   'profile': user, 'canrate': canrate, 'canbestintrest': canbestintrest, 'ratting': ratting}
        return render(request, 'judge/ratejudge.html', context)
    else:
        try:
            bestIntrest = bestInterest.objects.filter(ratedTo=pk)
            for b in bestIntrest:
                if b.user == request.user:
                    canbestintrest = False
        except User.DoesNotExist:
            bestIntrest = ''

        for r in ratting:
            if r.user == request.user:
                canrate = False
        context = {'judgeInfo': ratedTo,
                   'profile': user, 'canrate': canrate, 'canbestintrest': canbestintrest, 'ratting': ratting}
        return render(request, 'judge/ratejudge.html', context)


def bestIntrest(request, pk):
    canrate = True
    canbestintrest = True
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


def editRatting(request, pk):

    canrate = True
    canbestintrest = True
    judgeInfo = judge.objects.get(id=pk)
    inst = judgeRateing.objects.get(user=request.user, ratedTo=judgeInfo)
    if request.method == 'POST':
        form = judgeRateingForm(request.POST, instance=inst)
        form.save()
        if form.is_valid():
            form.save()
            profile = UserProfile.objects.get(user=request.user)
            ratting = judgeRateing.objects.filter(ratedTo=judgeInfo)
            profile = UserProfile.objects.get(user=request.user)
            ratting = judgeRateing.objects.filter(ratedTo=judgeInfo)
            total_num = (len(ratting))*5
            obtain_num = 0
            for r in ratting:
                obtain_num += r.rating
                if r.user == request.user:
                    canrate = False
            if total_num != 0:
                total_rating = (obtain_num/total_num)*5
            try:
                bestIntrest = bestInterest.objects.filter(ratedTo=judgeInfo)
                for r in bestIntrest:
                    if r.user == request.user:
                        canbestintrest = False

            except User.DoesNotExist:
                bestIntrest = ''
            context = {'judgeInfo': judgeInfo,
                       'profile': profile, 'ratting': ratting, 'total_rating': total_rating, 'canrate': canrate, 'canbestintrest': canbestintrest}
            return render(request, 'judge/ratejudge.html', context)
    return redirect('rateJudge/pk')


def getJudge2(request, pk):
    profile = ""
    user = request.user
    canrate = True
    canbestintrest = True
    total_rating = 0
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=user)
    judgeInfo = judge.objects.get(id=pk)
    try:
        ratting = judgeRateing.objects.filter(ratedTo=judgeInfo)
        total_num = (len(ratting))*5
        obtain_num = 0
        for r in ratting:
            obtain_num += r.rating
            if r.user == request.user:
                canrate = False
        if total_num != 0:
            total_rating = (obtain_num/total_num)*5

    except User.DoesNotExist:
        ratting = ''

    try:
        bestIntrest = bestInterest.objects.filter(ratedTo=judgeInfo)
        for r in bestIntrest:
            if r.user == request.user:
                canbestintrest = False
    except User.DoesNotExist:
        ratting = ''
    context = {'judgeInfo': judgeInfo,
               'profile': profile, 'ratting': ratting, 'total_rating': total_rating, 'canrate': canrate, 'canbestintrest': canbestintrest}
    template_name = "judge/ratejudge.html"
    return render(request, 'judge/ratejudge.html', context)


def updateRatting(pk):
    judgeInstance = judge.objects.get(id=pk)
    judgeInstance.totalRating = (
        judgeInstance.obtainScore/(judgeInstance.numberOfRatings*5))*5
    judgeInstance.save()
