from django.shortcuts import render

# Create your views here.
def students(request):
    stno="HELLO ARAVIND"
    my_dict={'stno':stno}
    return render(request,'home.html',my_dict)
