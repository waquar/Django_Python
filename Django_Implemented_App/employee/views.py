from django.shortcuts import render

# Create your views here.

def helloemployee(request):
    return render(request, 'secondapphtml.html')