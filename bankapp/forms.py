from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone_no', 'email', 'account', 'transact_amt']


class TransferMoney(forms.Form):
    amount = forms.IntegerField()

