from django.urls import path
from login_portal import views

urlpatterns = [
    path('',views.index,name='home'),
]
