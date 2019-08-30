from django.shortcuts import render, redirect, HttpResponse
from django.views import View

from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from .models import Problem, Solution

home = 'http://127.0.0.1:8003/'


def problem_valid(post):
    return True

def solution_valid(post):
    return True

#class Problems(LoginRequiredMixin, View):
class Problems(View):

    def get (self, request):

        return render(request, 'main.html', context = {
            'Problem': Problem.objects.all().order_by('-likes'),
            'Solution': Solution.objects.all().order_by('-likes')
        })

    def post (self, request):
        #Save new problem
        if request.POST.get('text'):
            if problem_valid(request.POST):
                l_p = Problem.objects.all().count()+1
                p = Problem(
                    text = request.POST['text'],
                    number = l_p,
                    likes = 0,
                    )
                p.save()

        #Save new solution
        if request.POST.get('textS'):
            if solution_valid(request.POST):
                l_s = Solution.objects.all().count()+1
                p_n = request.POST['problem']
                problem = Problem.objects.get(number = p_n)
                print(problem) 
                s = Solution(
                    text = request.POST['textS'],
                    number = l_s,
                    problem = problem,
                    )
                s.save()

        #Save new problem like
        if request.POST.get('prolike'):
            p_n = request.POST['prolike']
            NL=Problem.objects.get(number = p_n)             
            NL.likes+=1
            NL.save()

        #Save new problem like
        if request.POST.get('sollike'):
            s_n = request.POST['sollike']
            NL = Solution.objects.get(number = s_n)
            NL.likes += 1
            NL.save()
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
        return HttpResponse('Already signed-up')
