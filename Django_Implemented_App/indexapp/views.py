from django.shortcuts import render, redirect
from indexapp.models import Bank, Customer
from indexapp.forms import  bankform, customerform
from django.contrib.auth.decorators import login_required

def create_customer(request):
    form = customerform()

    if request.method == 'POST':
        form = customerform(request.POST)
        if form.is_valid():
            #form.save()        it will also save the data but  if we want to make any further validation  in future then thiss might be useless.

            form.save()
            return  redirect('customer_index')

    return  render(request, 'customer/create.html', {'form': form})

def views(request, pk):
    data = Bank.objects.get(id = pk)
    return  render(request, 'view.html', {'data': data })

def delete(request, pk):
    data = Bank.objects.get(id =pk)
    data.delete()
    #delete data where id =pk
    return  redirect('index')

def update(request,pk):

    data = Bank.objects.get(id = pk)
    form = bankform(instance=data)

    if request.method == 'POST':
        form = bankform(request.POST, instance=data)
        if form.is_valid():
            #form.save()        it will also save the data but  if we want to make any further validation  in future then thiss might be useless.
            bank = Bank()
            bank.id = pk
            bank.name = form.cleaned_data['name']
            bank.email = form.cleaned_data['email']
            bank.address = form.cleaned_data['address']
            bank.save()
            return  redirect('index')

    return  render(request, 'update.html', {'form': form})

def create(request):
    form = bankform()

    if request.method == 'POST':
        form = bankform(request.POST)
        if form.is_valid():
            #form.save()        it will also save the data but  if we want to make any further validation  in future then thiss might be useless.
            bank = Bank()
            bank.name = form.cleaned_data['name']
            bank.email = form.cleaned_data['email']
            bank.address = form.cleaned_data['address']
            bank.save()
            return  redirect('index')

    return  render(request, 'create.html', {'form': form})

@login_required(login_url='/signin')                 #using decorators
def index(request):                                                   #displaying database to user
    data = Bank.objects.all()
    #data = Bank.objects.raw('select * from Bank')                            we can also use raw sql input using raw
    return  render(request, 'index.html', {'data': data })

def customer_index(request):                                                   #displaying database to user
    data = Customer.objects.all()
    #data = Bank.objects.raw('select * from Bank')                            we can also use raw sql input using raw
    return  render(request, 'customer/index.html', {'data': data })

def update_customer(request, pk):
    data = Customer.objects.get(id = pk)
    form = customerform(request.POST, instance=data)

    if request.method == 'POST':
        form = customerform(request.POST, instance=data)
        if form.is_valid():
            customer = Customer()
            customer.name = form.cleaned_data['name']
            customer.email = form.cleaned_data['bank']
            customer.address = form.cleaned_data['email']
            customer.save()
            return redirect('customer/index')

    return render(request, 'customer/update.html', {'form': form})



def customer_view(request, pk):
    data = Customer.objects.get(id = pk)       #fetchig the  data inside Customer
    return  render(request, 'customer/view.html', {'data': data })

def customer_delete(request, pk):
    data = Customer.objects.get(id =pk)
    data.delete()
    #delete data where id =pk
    return  redirect('customer/index')






