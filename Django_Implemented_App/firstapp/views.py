from django.shortcuts import render
from firstapp.forms import  formExample, coreForm

def core_html(request):
    form= coreForm()

    if request.method == "POST":
        form = coreForm(request.POST)

        if form.is_valid():
            pass

    return  render(request, 'coreHtml.html', {'form': form})

def formexample(request):
    form = formExample()

    if request.method == 'POST':
        form = formExample(request.POST)
        if form.is_valid():
            pass
    return render(request, 'formhtml.html', {'form' : form})


def hello(request):
    l1 = [1,2,3,4,5,6]
    d1 = {'a':'1' , 'b':'2', 'c':'3'}
    return render(request, 'hello.html' , { 'dict':d1,'listdata' : l1, 'name' : 'xyz' , 'email': 'xyz@gmail.com'})

def django_layout(request):
    return  render(request, 'hellosecond.html')





