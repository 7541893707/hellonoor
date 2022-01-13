from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def noor(request):
    data={"name": "noor" ,  "place":"bhore"}
    return render(request,"template1.html",data)

def sum(request):
  
  numm1= int(request.GET["num1"])
  numm2= int(request.GET["num2"])
  sum=numm1 + numm2

  return render(request,'result.html',{"res": sum})