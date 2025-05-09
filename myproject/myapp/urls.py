from django.urls import path
from . import views

urlpatterns = [
    path('',view=views.index, name='index'),
    path('all-lists/', view=views.allLists, name='all-lists'),
    path('done-lists/', view=views.doneLists, name='done-lists'),
]