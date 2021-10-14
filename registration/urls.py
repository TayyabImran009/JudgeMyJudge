from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.loginPage, name="loginPage"),

    path('register/', views.registerUser, name="register"),

    path('logout/', views.logoutUser, name="logout"),

    path('home/', views.home, name="home"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="registration/rest_password.html"),
         name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_change_confirm_message.html"),
         name="password_reset_complete"),

]
