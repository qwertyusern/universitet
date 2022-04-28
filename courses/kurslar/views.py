from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *

def asosiy(request):
    return render(request,"asosiy.html")

def ustoz(request):
    u=Ustoz.objects.all
    if request.method == "POST":
        Ustoz.objects.create(
            ism=request.POST.get("ism"),
        )
        return redirect("/ustoz/")
    return render(request, "ustoz.html",{"us":u})

def fan(request):
    f=Fan.objects.all
    return render(request, "fan.html",{"fan":f})

def yonalish(request):
    f=Yonalish.objects.all
    return render(request, "yonalish.html",{"yonalish":y})


