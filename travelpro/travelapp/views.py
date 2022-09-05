from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, People


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=People.objects.all()
    return render(request,'index.html',{'result':obj,'people':obj1})

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     result=x+y
#     return render(request,'result.html',{'result':result})

