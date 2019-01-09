from django.urls import path
from password_reset import views

urlpatterns = [
    path('',views.index,name='reset'),
]
