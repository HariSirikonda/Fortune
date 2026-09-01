from django.shortcuts import redirect, render
from core.forms import TransactionForm

def home(request):
    return render(request, 'home.html')

def addTransaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TransactionForm()
    return render(request, 'transactionPage.html', {'form': form})