from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone_no = models.IntegerField(null=True)
    email = models.EmailField(max_length=50)
    account = models.CharField(max_length=10)
    transact_amt = models.IntegerField(null=True)
    balance = models.IntegerField(null=True)

    def __str__(self):
        return self.name