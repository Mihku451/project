import json

from polls.forms import SignUpForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect

# Create your views here.
from polls.models import Exercise, Question, Answer


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


def create_exercise(request):
    if request.method == 'POST':
        creator = request.user
        name = request.POST["name"]
        time = request.POST["time"]
        limit_of_tries = request.POST["limit_of_tries"]
        ex = Exercise(creator=creator, name=name, time=time, limit_of_tries=limit_of_tries)
        ex.save()
        return redirect('create_exercise_st2', ex.id)
    return render(request, 'Exercise_create.html')


def create_exercise_st2(request, id):

    if request.method == 'POST':
        title = request.POST.get('question')
        exercise = get_object_or_404(Exercise, pk=id)
        image = request.POST.get('file')
        score=request.POST.get('score')

        data = json.loads(request.POST.get('answers', ''))
        question = Question(question_text=title, exercise=exercise, image=image,score=score)

        for answer in data:
            answer = Answer(question=question, answer_text=answer['text'], answer_type=answer['type'],
                         is_valid=['correct_input'])
            answer.save()
        return render(request, "Exercise_create_st1.html")

    elif request.method == 'GET':
        return render(request, "Exercise_create_st1.html")


def exercise_passing(request, id):
    context = {}
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        exercise = get_object_or_404(Exercise, pk=id)
        questions = []
        questions_answers = []
        for question in exercise.question_set.all():
            questions.append(question)
            answers = []
            for answer in question.answer_set.all():
                answers.append(answer)
            context['questions_answers'].append(
                {
                    'question': question,
                    'answers': answers,
                }
            )

        # {{% for qa in questions_answers %}}
        # <li>{{qa.question}}</li>
        # {{% for answer in qa.answers %}}
        # {{% endfor %}}
        # {{% endfor %}}
        #
        context = {
            'exercise': exercise,

            'questions_answers': questions_answers,

        }
    return render(request, "view_Exercise.html")