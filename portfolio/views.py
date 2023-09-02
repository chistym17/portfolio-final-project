from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # Your view logic here
    return render(request, 'index.html')
