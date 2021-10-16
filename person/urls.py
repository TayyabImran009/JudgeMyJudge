from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('changePassword/', views.changePassword, name="changePassword"),

]
