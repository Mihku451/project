from polls.forms import SignUpForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect


# Create your views here.
def index(request):
    return render(request, "index.html")


def Logout(request):
    logout(request)
    return redirect("/")


def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.refresh_from_db()
            new_user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=new_user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


def SignIn(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            context['error'] = "ошибка при входе"
    return render(request, 'login.html', context)


def create_exerecise(request):
    return render(request, 'login.html')
