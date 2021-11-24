from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('SignUp', views.SignUp, name='SignUp'),
    path('login', views.SignIn, name="login"),
    path('logout',views.logout, name="logout")

]
