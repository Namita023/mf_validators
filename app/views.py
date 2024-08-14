from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.

def insert_stud(request):
    d={'ESFO':StudentMF()}
    if request.method=="POST":
        SDFO=StudentMF(request.POST)
        if SDFO.is_valid():
            SDFO.save()
            return HttpResponse('Data inserted')
        else:
            return HttpResponse('Invalid data')
    return render(request,"insert_stud.html",d)
