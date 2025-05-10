from django.urls import path
from . import views

urlpatterns = [
    path('',view=views.index, name='index'),
    path('all-lists/', view=views.allLists, name='all-lists'),
    path('done-lists/', view=views.doneLists, name='done-lists'),
    path('add-list/', view=views.addList, name='add-list'),
    path('edit-list/<int:id>/', view=views.editList, name='edit-list'),
    path('view-list/<int:id>/', view=views.viewList, name='view-list'),
    path('delete-list/<int:id>/', view=views.deleteList, name='delete-list'),
]