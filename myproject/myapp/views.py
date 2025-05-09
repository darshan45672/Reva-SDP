from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the myapp index.")
    context = {
        'title': 'Welcome to MyApp',
        'message': 'This is the index page of myapp.',
    }

    return render(request, 'index.html', context)

def about(request):
    return HttpResponse("This is the about page of myapp.")

def contact(request):
    return HttpResponse("This is the contact page of myapp.")