from django.shortcuts import render, redirect, HttpResponse
from django.views import View

from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from .models import Problem, Solution

home = 'http://127.0.0.1:8000/'

def problem_valid(post):
    return True

def solution_valid(post):
    return True

class Problems(LoginRequiredMixin, View):

    def get (self, request):
        return render(request, 'main.html', context = {
            'Problem': Problem.objects.all(),
            'Solution': Solution.objects.all()
        })


@login_required
def addp (request):
    if request.method == 'POST':
        if problem_valid(request.POST):
            l_p = Problem.objects.all().count()
            p = Problem(
                text = request.POST['text'],
                number = l_p,
                )
            p.save()
            return redirect (home)
    return render (request, 'addp.html')
    
@login_required
def adds (request):
    if request.method == 'POST':
        if request.POST.get('text'):
            if solution_valid(request.POST):
                l_s = Solution.objects.all().count()  
                p_n = request.POST['problem']
                problem = Problem.objects.get(number = p_n)
                print(problem) 
                s = Solution(
                    text = request.POST['text'],
                    number = l_s,
                    problem = problem,
                    )
                s.save()
                return redirect (home)

        if request.POST['problem']:
            return render (request, 'adds.html', context = {'problem': request.POST['problem']})
    return redirect (home)

def sign_up (request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect(home)
        else:
            form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
    else:
        return HttpResponse('Already signup-ed')
