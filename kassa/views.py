from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def navbar(request):
    return render(request, 'navbar.html')

def hotels(request):
    return render(request, 'hotels.html')

def termsofuse(request):
    return render(request, 'termsofuse.html')

def refund(request):
    return render(request, 'refund.html')

    
