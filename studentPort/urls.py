from django.urls import path
from studentPort import views

urlpatterns = [
    path('',views.index,name='studentPort'),
]
