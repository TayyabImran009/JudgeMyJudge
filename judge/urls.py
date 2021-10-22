from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    # path('load/', views.loadData, name='load'),

    # path('removeSpace/', views.removeSpace, name='removeSpace'),

    path('autocomplete/', views.autocomplete, name="autocomplete"),

    path('autocompleteLocation/', views.autocompleteLocation,
         name="autocompleteLocation"),

    path('getJudgeByLocation/<str:name>', views.getJudgeByLocation,
         name="getJudgeByLocation"),

    path('getJudge/', views.getJudge, name="getJudge"),

    path('rateJudge/<str:pk>/', views.rateJudge, name="rateJudge"),

    path('bestIntrest/<str:pk>/', views.bestIntrest, name="bestIntrest"),

    path('editRatting/<str:pk>/', views.editRatting, name="editRatting"),

    path('autocomplete2/<str:pk>', views.autocomplete2, name="autocomplete2"),

    path('getJudge2/<str:pk>', views.getJudge2, name="getJudge2"),

    path('autocomplete3/<str:pk>', views.autocomplete3, name="autocomplete3"),

]
