from django.shortcuts import render

# Create your views here.

def landing(request):
    return render(
        request,
        'single_pages/landing.html'
    )

def find(request):
    return render(
        request,
        'single_pages/find.html'
    )