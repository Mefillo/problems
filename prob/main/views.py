from django.shortcuts import render, redirect, HttpResponse
from django.views import View

from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.middleware.csrf import get_token

from .models import Problem, Solution, Utoken

home = 'http://127.0.0.1:8000/'


def problem_valid(post):
    return True

def solution_valid(post):
    return True

def problem_already_liked (ut, p_n):
    '''Check if problem already liked/exist in dictionary of User'''
    if p_n in ut.problems.keys():
        return ut.problems[p_n]
    else:
        ut.problems.update({p_n : False})
        ut.save()
        return False

def solution_already_liked (ut, s_n):
    '''Check if solution already liked/exist in dictionary of User'''
    if s_n in ut.solutions.keys():
        return ut.solutions[s_n]
    else:
        ut.solutions.update({s_n : False})
        ut.save()
        return False

class Problems(LoginRequiredMixin, View):

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
            #Get User
            try:
                ut = Utoken.objects.get(user = request.user)
            except Utoken.DoesNotExist:
                ut = Utoken(user = request.user)
                ut.save()
            #Get Problem
            p_n = request.POST['prolike']
            pr=Problem.objects.get(number = p_n)
            #Check if problem liked already
            if problem_already_liked(ut, p_n):
                ut.problems[p_n] = False
                ut.save()
                pr.likes-=1
                pr.save()
            else:
                ut.problems[p_n] = True
                ut.save()
                pr.likes+=1 
                pr.save()
            return redirect (home)



        #Save new solution like
        if request.POST.get('sollike'):
            #Get User
            try:
                ut = Utoken.objects.get(user = request.user)
            except Utoken.DoesNotExist:
                ut = Utoken(user = request.user)
                ut.save()
            #Get Solution
            s_n = request.POST['sollike']
            sol = Solution.objects.get(number = s_n)
            #Check if solution liked already
            if solution_already_liked(ut, s_n):
                ut.solutions[s_n] = False
                ut.save()
                sol.likes-=1
                sol.save()
            else:
                ut.solutions[s_n] = True
                ut.save()
                sol.likes+=1 
                sol.save()
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
