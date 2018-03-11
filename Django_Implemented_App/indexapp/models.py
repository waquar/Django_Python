from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30, unique=True)
    address = models.CharField(max_length=260)

    def __str__(self):
        return  self.name

    class Meta:

        db_table = 'bank'

class Customer(models.Model):

    name = models.CharField(max_length=30)
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT)              #on_delete=models.PROTECT used for avoiding delete from another table
    email = models.EmailField(max_length=50, unique= True)

    class Meta:

        db_table = 'customer'

