from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ListForm
from .models import List

# Create your views here.
def index(request):
    lists = List.objects.all()
    return render(request, 'index.html', {'lists': lists})

def allLists(request):
    return render(request, 'allLists.html')

def doneLists(request):
    return render(request, 'doneLists.html')

def addList(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all-lists')
    else:
        form = ListForm()
        
    return render(request, 'addList.html', {'form': form})

def editList(request, id):
    list = get_object_or_404(List, id=id)
    if request.method == 'POST':
        form = ListForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('all-lists')
    else:
        form = ListForm(instance=list)
    return render(request, 'editList.html', {'form': form, 'list': list})

def viewList(request, id):
    list = get_object_or_404(List, id=id)
    return render(request, 'viewList.html', {'list': list})

def deleteList(request, id):
    list = get_object_or_404(List, id=id)
    if request.method == 'POST':
        list.delete()
        return redirect('all-lists')
    else:
        return redirect('all-lists')