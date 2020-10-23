from django.shortcuts import render
from django.http import HttpResponse
from importlib.resources import path
import subprocess

# Create your views here.
def Cal(request):
    return render(request, "Calculator/NewWeedCal.html",{
        
    })

def compute(request):
    return render(request, "Calculator/Compute.html",{
        
    })

