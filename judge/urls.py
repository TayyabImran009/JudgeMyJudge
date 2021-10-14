from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('load/', views.loadData, name='load'),

    path('autocomplete/', views.autocomplete, name="autocomplete"),

    path('getJudge/', views.getJudge, name="getJudge"),
]