from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'main/1.html')
    
def about(request):
    return HttpResponse("<h4>ZeroFrames is an easy-to-use tool for creating custom graphics for your Flipper Zero. You can design icons, frames, and other visuals to personalize your device. The tool lets you preview your designs in real-time, export them easily, and even share them with others.</h4>")
    