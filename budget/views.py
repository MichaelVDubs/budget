from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

from .models import Loan, User
from .forms import LoanForm, UserForm

# Create your views here.
def index(request):
    return render(request, 'budget/index.html')

def adduser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            confirm = form.cleaned_data['confirm']
            user = form.save(commit=False)
            if user.password == confirm:
                user.set_password(user.password)
                user = form.save()
                request.session['user'] = user.pk
                request.session['name'] = user.username
            else:
                form = UserForm()
                return render(request, 'budget/adduser.html', {'form':form})
            return redirect('loanview')
    else:
        form = UserForm()
    return render(request, 'budget/adduser.html', {'form':form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                request.session['user'] = user.pk
                request.session['name'] = user.username
                return redirect('loanview')
            else:
                HttpResponse("General Kenobi...")
    else:
        form = AuthenticationForm()
    return render(request, 'budget/login.html', {'form':form})

def logout(request):
    del request.session['user']
    del request.session['name']
    return redirect('index')

def loanview(request):
    if 'user' in request.session:
        all_loans = Loan.objects.filter(user_id=request.session['user']).order_by('begin_date')
        context = {'all_loans': all_loans}
        return render(request, 'budget/loanview.html', context)
    return redirect('index')

def loanDetail(request, loan_id):
    loan = Loan.objects.get(id=loan_id)
    return HttpResponse('This is loan ' + loan.name)

def addloan(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            if 'user' in request.session:
                loan = form.save(commit=False)
                user = User.objects.get(pk=request.session['user'])
                loan.user_id = user
                loan.save()
                return redirect('loanview')
            return redirect('index')
    else:
        form = LoanForm()
    return render(request, 'budget/addloan.html', {'form':form})

def loanedit(request, pk):
    loan = Loan.objects.get(pk=pk)
    if request.method == 'POST':
        form = LoanForm(request.POST, instance=loan)
        if form.is_valid():
            post = form.save(commit=False)
            user = User.objects.get(pk=1)
            post.user_id = user
            post.save()
            return redirect('loanview')
    else:
        form = LoanForm(instance=loan)
    return render(request, 'budget/addloan.html', {'form':form})

def loandelete(request, pk):
    loan = Loan.objects.get(pk=pk)
    loan.delete()
    return redirect('loanview')
