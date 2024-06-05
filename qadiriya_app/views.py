from django.shortcuts import render, redirect  
from django.http import HttpResponse


def dashboard(request):
     return render(request, 'qadiriya_app/dashboard.html') 


def abdulqadir(request):
     return render(request,'qadiriya_app/abdul-qadir.html' )


def uwesuAhmad(request):
     return render(request,'qadiriya_app/uwesu-ahmad.html' )


def mohdNasor(request):
     return render(request,'qadiriya_app/mohd-nasor.html' )



def tawasuliKubwa(request):
     return render(request,'qadiriya_app/tawasuli-kubwa.html' )



def fathaMashekhe(request):
     return render(request,'qadiriya_app/fatha-mashekhe.html' )
