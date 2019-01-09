from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'User': "Piyush Ranjan"}
    return render(request, 'user.html', context = my_dict)
