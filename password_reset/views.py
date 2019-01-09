from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict ={'insert_me':"hello"}
    return render(request,'forgotpassword.html',context=my_dict)
