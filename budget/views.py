from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from .models import Loan, User
from .forms import LoanForm

# Create your views here.
def index(request):
    return render(request, 'budget/index.html')

def loanview(request):
    all_loans = Loan.objects.order_by('begin_date')
    context = {'all_loans': all_loans}
    return render(request, 'budget/loanview.html', context)

def loanDetail(request, loan_id):
    loan = Loan.objects.get(id=loan_id)
    return HttpResponse('This is loan ' + loan.name)

def addloan(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            user = User.objects.get(pk=1)
            post.user_id = user
            post.save()
            return redirect('loanview')
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
