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

def allLists(request):
    return render(request, 'allLists.html')

def doneLists(request):
    return render(request, 'doneLists.html')