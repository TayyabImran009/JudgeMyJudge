from django.shortcuts import render, redirect
import csv
from .models import judge
# Create your views here.


def loadData(request):
    with open('data.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            judge.objects.create(location=row[0], general_district_court=row[1], position1=row[2],
                                 juvenile_domestic_court=row[3], position2=row[4], circuit_court=row[5], position3=row[6])
    return render(request, 'home.html')
