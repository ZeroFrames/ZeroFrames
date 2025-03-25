from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'main/1.html')

def about(request):
    return render(request,'main/2.html')
    
def button(request):
    return render(request,'main/3.html')    
def paint(request):
    return render(request,'main/ris.html')
 