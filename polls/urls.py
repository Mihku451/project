from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('SignUp', views.SignUp, name='SignUp'),
    path('login', views.SignIn, name="login"),
    path('logout', views.logout, name="logout"),
    path('create_exercise', views.create_exercise, name='create_exercise'),
    path('create_exercise/<int:id>', views.create_exercise_st2, name='create_exercise_st2'),
    path('exercise_passing/<int:id>', views.exercise_passing, name='exercise_passing'),

]
