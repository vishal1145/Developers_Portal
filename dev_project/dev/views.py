from django.shortcuts import render

def index(request):
   
    return render(request, 'dev/home.html')

def faq(request):
   
    return render(request, 'dev/faq.html')