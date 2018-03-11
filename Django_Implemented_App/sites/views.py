from django.shortcuts import render, redirect
from django.contrib.auth import  login,logout,authenticate
from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm
from sites.forms import LoginForm
from django.contrib.auth.decorators import  login_required

def staticExample(request):                                                                                     #for static example
    return  render(request, 'static_example.html')

def signup(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = User()
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password1'])
            #user.set_password =f orm.cleaned_data['password1'])   it will save directly in table showing credentials .
            user.save()
            request.session['message'] = 'Registration done sucessfully!!!!'
            #return  render(request,  'signup.html',  { 'form': form, 'msg' : 'Registration Done SuccessFully!!!'  })
            return  redirect('signin')                             #setting session variable for one time message popup
    return  render(request, 'signup.html', {'form' : form, 'msg': ''})

def signin(request):

    if request.user.is_authenticated:                                   #for continuing the older session if user alrey logged in
        return  redirect('dashboard')

    form  = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)

            if user is None:
                return  render(request, 'signin.html', {'form' : form, 'msg':  'user not found'})
            else:
                login(request, user)
                return redirect('dashboard')

    if 'message' in request.session:                                            #setting session variable condition
        msg = request.session['message']
        del request.session['message']
        return  render(request, 'signin.html', {'form': form, 'msg' : msg})
    else:
        return render(request, 'signin.html', {'form': form, 'msg': ''})


def logoutfunction(request):
    logout(request)
    return   redirect('signin')


@login_required(login_url='/signin')                      #signin must be the regex in urls
def dashboard(request):
    return  render(request, 'dashboard.html')
