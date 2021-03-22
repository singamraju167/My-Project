from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerForm, TransferMoney


def home(request):
    return render(request, 'bankingApp/home.html')


def view_customers(request):
    all_customers = Customer.objects.all()
    context = {
        "all_customers": all_customers
    }

    return render(request, 'bankingApp/index.html', context)


'''def Customer_form(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        user_id = request.POST.get('all_customers.id')
        print(user_id)

        if form.is_valid():
            # form.save()
            nm = form.cleaned_data['name']
            pn = form.cleaned_data['phone_no']
            em = form.cleaned_data['email']
            ac = form.cleaned_data['account']
            tm = form.cleaned_data['transact_amt']
            data = Customer(name=nm, phone_no=pn, email=em, account=ac, transact_amt=tm)
            data.save()
            return HttpResponse('Details added successfully!')
    else:
        form = CustomerForm()
    return render(request, 'bankingApp/customer_form.html', {'form': form})'''


def details(request, user_id):
    data = Customer.objects.get(id=user_id)
    return render(request, 'bankingApp/data.html', {'data': data, 'user_id': user_id})


def transfer_money(request, user_id):
    all_customers = Customer.objects.all()
    user = Customer.objects.get(id=user_id)
    bal = user.balance
    print(user.id)
    if request.method == 'POST':
        form = TransferMoney(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            data = Customer(id=user_id, name=user.name, phone_no=user.phone_no, email=user.email, account=user.account, transact_amt=amount, balance=amount+bal)
            data.save()
            return HttpResponse('Update')

    else:
        form = TransferMoney()
    return render(request, 'bankingApp/transfer.html', {'form': form, 'all_customers': all_customers, 'username': user.name, 'user_id':user.id})


def addMoney(request, user_id, user):
    all_customers = Customer.objects.all()
    sen = Customer.objects.get(id=user)
    rec = get_object_or_404(Customer, id=user_id)
    bal = rec.balance
    if request.method == 'POST':
        print(rec, sen)
        form = TransferMoney(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            prev_data = Customer(id=user, name=sen.name, phone_no=sen.phone_no, email=sen.email, account=sen.account,transact_amt=0-amount, balance=sen.balance-amount)
            data = Customer(id=user_id, name=rec.name, phone_no=rec.phone_no, email=rec.email, account=rec.account, transact_amt=amount, balance=amount+bal)
            data.save()
            prev_data.save()
            return redirect('view_customers')

    else:
        form = TransferMoney()
    return render(request, 'bankingApp/add.html', {'form': form, 'all_customers': all_customers, 'rec': rec.name})

