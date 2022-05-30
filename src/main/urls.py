from django.urls import path
from .views import ToDoView, Check, Remove, Add



urlpatterns = [
    path('', ToDoView.as_view(), name='main'),
    path('check/', Check.as_view(), name='check'),
    path('remove/', Remove.as_view(), name='remove'),
    path('add/', Add.as_view(), name='add'),
]