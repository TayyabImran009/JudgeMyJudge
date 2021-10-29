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
            state__istartswith=request.GET.get('term'))
        searchJudge = list()
        for j in judgeList:
            if j.state not in searchJudge:
                searchJudge.append(j.state)
        return JsonResponse(searchJudge, safe=False)


def autocomplete2(request, pk):
    if 'JudgeLocation' not in request.session:
        j = judge.objects.filter(
            name__istartswith=pk).values()
    else:
        j = judge.objects.filter(
            name__istartswith=pk, state=request.session["JudgeLocation"]).values()
    jugeslist = list(j)

    return JsonResponse({'jugeslist': jugeslist})


def judgeWithLocation(request, pk):
    if 'JudgeLocation' not in request.session:
        j = judge.objects.filter(
            name__istartswith=pk).values()
    else:
        j = judge.objects.filter(
            name__istartswith=pk, state=request.session["JudgeLocation"]).values()
    jugeslist = list(j)

    return JsonResponse({'jugeslist': jugeslist})


def autocomplete3(request, pk):
    judgesList = judge.objects.filter(
        state__istartswith=pk)
    locationlist = list()
    for l in judgesList:
        if l.state not in locationlist:
            locationlist.append(l.state)
    print("Hello")
    print(locationlist)
    return JsonResponse({'locationlist': locationlist})


def getJudgeByLocation(request, name):
    judgeList = judge.objects.filter(location=name)
    location = judgeList[0].location
    context = {'judgeList': judgeList, 'location': location}
    return render(request, 'judge/judgesByLocation.html', context)


# def getJudge(request):
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
    category_list = categories.objects.all()
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
        category = categories.objects.get(name=request.POST['category'])
        tag1 = request.POST['tag1']
        tag2 = request.POST['tag2']
        tag3 = request.POST['tag3']
        ratedTo.numberOfRatings += 1
        ratedTo.obtainScore += rating
        ratedTo.save()

        r = judgeRateing(user=user, ratedTo=ratedTo, rating=rating, description=description,
                         cannon1=cannon1, cannon2=cannon2, cannon3=cannon3, cannon4=cannon4, cannon5=cannon5, political_perspective_of_judge=political_perspective_of_judge, family_connections_in_legal_community=family_connections_in_legal_community, category=category, tag1=tag1, tag2=tag2, tag3=tag3)
        r.save()

        updateRatting(pk)

        if tag1 != "":
            t1 = tags.objects.get(name=tag1)
            if judgeTags.objects.filter(tag=t1, tagTo=ratedTo).exists():
                judgeTags.objects.get(
                    tag=t1, tagTo=ratedTo).user.add(request.user)
            else:
                jt = judgeTags.objects.create(tag=t1, tagTo=ratedTo)
                jt.user.add(request.user)
                jt.save

        if tag2 != "":
            t2 = tags.objects.get(name=tag2)
            if judgeTags.objects.filter(tag=t2, tagTo=ratedTo).exists():
                judgeTags.objects.get(
                    tag=t2, tagTo=ratedTo).user.add(request.user)
            else:
                jt = judgeTags.objects.create(tag=t2, tagTo=ratedTo)
                jt.user.add(request.user)
                jt.save

        if tag3 != "":
            t3 = tags.objects.get(name=tag3)
            if judgeTags.objects.filter(tag=t3, tagTo=ratedTo).exists():
                judgeTags.objects.get(
                    tag=t3, tagTo=ratedTo).user.add(request.user)
            else:
                jt = judgeTags.objects.create(tag=t3, tagTo=ratedTo)
                jt.user.add(request.user)
                jt.save

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

        return redirect('/getJudge2/'+str(ratedTo.id))
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
        tagList = judgeTags.objects.filter(tagTo=ratedTo)
        return redirect('/getJudge2/'+str(ratedTo.id))


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
            return redirect('/getJudge2/'+str(judgeInfo.id))
    else:
        judgeInfo = judge.objects.get(id=pk)
        profile = UserProfile.objects.get(user=request.user)
        ratting = judgeRateing.objects.filter(ratedTo=judgeInfo)
        context = {'judgeInfo': judgeInfo,
                   'profile': profile, 'ratting': ratting}
        return redirect('/getJudge2/'+str(judgeInfo.id))


def editRatting(request, pk):

    canrate = True
    canbestintrest = True
    judgeInfo = judge.objects.get(id=pk)
    inst = judgeRateing.objects.get(user=request.user, ratedTo=judgeInfo)
    profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = judgeRateingForm(request.POST, instance=inst)
        print(form.errors)
        if form.is_valid():
            rtForm = form.save(commit=False)
            if rtForm.tag1 == None:
                rtForm.tag1 = ""
            if rtForm.tag2 == None:
                rtForm.tag2 = ""
            if rtForm.tag3 == None:
                rtForm.tag3 = ""
            rtForm.category = categories.objects.get(
                name=request.POST['category'])
            rtForm.save()
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

            tag1 = request.POST['tag1']
            tag2 = request.POST['tag2']
            tag3 = request.POST['tag3']

            t1 = None
            t2 = None
            t3 = None

            if(tag1 != ""):
                t1 = tags.objects.get(name=tag1)
            if(tag2 != ""):
                t2 = tags.objects.get(name=tag2)
            if(tag3 != ""):
                t3 = tags.objects.get(name=tag3)

            if tag1 != "":
                if judgeTags.objects.filter(tag=t1, tagTo=judgeInfo).exists():
                    judgeTags.objects.get(
                        tag=t1, tagTo=judgeInfo).user.add(request.user)
                else:
                    jt = judgeTags.objects.create(tag=t1, tagTo=judgeInfo)
                    jt.user.add(request.user)
                    jt.save

            if tag2 != "":
                if judgeTags.objects.filter(tag=t2, tagTo=judgeInfo).exists():
                    judgeTags.objects.get(
                        tag=t2, tagTo=judgeInfo).user.add(request.user)
                else:
                    jt = judgeTags.objects.create(tag=t2, tagTo=judgeInfo)
                    jt.user.add(request.user)
                    jt.save

            if tag3 != "":
                if judgeTags.objects.filter(tag=t3, tagTo=judgeInfo).exists():
                    judgeTags.objects.get(
                        tag=t3, tagTo=judgeInfo).user.add(request.user)
                else:
                    jt = judgeTags.objects.create(tag=t3, tagTo=judgeInfo)
                    jt.user.add(request.user)
                    jt.save

            jt = judgeTags.objects.filter(user=request.user, tagTo=judgeInfo)

            chkjt = [t1, t2, t3]

            for cjt in jt:
                if cjt.tag not in chkjt:
                    cjt.user.remove(request.user)
                    if cjt.user.exists():
                        print("Yes It has something")
                    else:
                        cjt.delete()
            return redirect('/getJudge2/'+str(judgeInfo.id))
    return redirect('/getJudge2/'+str(judgeInfo.id))


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
    listOfTags = tags.objects.all()
    category_list = categories.objects.all()
    request.session["JudgeLocation"] = judgeInfo.state
    tagList = judgeTags.objects.filter(tagTo=judgeInfo)
    userTag = []
    if request.user.is_authenticated:
        uTag = judgeTags.objects.filter(tagTo=judgeInfo, user=request.user)
        for uT in uTag:
            userTag.append(uT.tag.name)
    context = {'judgeInfo': judgeInfo,
               'profile': profile, 'ratting': ratting, 'total_rating': total_rating, 'canrate': canrate, 'canbestintrest': canbestintrest, 'categories': category_list, 'listOfTags': listOfTags, 'tagList': tagList, 'userTag': userTag}
    return render(request, 'judge/ratejudge.html', context)


def updateRatting(pk):
    judgeInstance = judge.objects.get(id=pk)
    judgeInstance.totalRating = (
        judgeInstance.obtainScore/(judgeInstance.numberOfRatings*5))*5
    judgeInstance.save()


@csrf_exempt
def likereview(request):
    rating = judgeRateing.objects.get(id=request.POST['id'])

    r = rating.dislikeBy.all()
    if request.user in r:
        rating.dislikeBy.remove(request.user)
        rating.total_dislikes -= 1.0

    rating.likeBy.add(request.user)
    rating.total_likes += 1.0
    rating.save()

    return JsonResponse({'totalDislikes': rating.total_dislikes, 'totalLikes': rating.total_likes})


@csrf_exempt
def dislikeReview(request):
    rating = judgeRateing.objects.get(id=request.POST['id'])

    r = rating.likeBy.all()
    if request.user in r:
        rating.likeBy.remove(request.user)
        rating.total_likes -= 1.0

    rating.dislikeBy.add(request.user)
    rating.total_dislikes += 1.0
    rating.save()

    return JsonResponse({'totalDislikes': rating.total_dislikes, 'totalLikes': rating.total_likes})


def setLocation(request, name):
    request.session["JudgeLocation"] = name
    return JsonResponse({'state': 1})
