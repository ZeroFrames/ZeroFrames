from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'main/1.html')

def about(request):
    return render(request,'main/2.html')
    
def stepa(request):
    return render(request,'main/3.html')     