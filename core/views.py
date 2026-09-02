from django.shortcuts import redirect, render
from core.forms import TransactionForm
from core.models import Transaction

def home(request):
    return render(request, 'core/home.html')

def allTransactions(request):
    transactions = Transaction.objects.all()
    context = {'transactions' : transactions}
    return render(request, 'core/allTransactions.html', context)

def addTransaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TransactionForm()
    return render(request, 'core/transactionPage.html', {'form': form})