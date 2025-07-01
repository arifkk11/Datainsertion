from django.shortcuts import render,redirect
from django.http import HttpResponse
from datainsertapp.models import *

# Create your views here.

def data(request):
    if request.method=='POST':
        names = request.POST['name']
        ages = request.POST['age']
        addresss = request.POST['address']
        x=Data.objects.create(Name=names,Age=ages,Address=addresss)
        x.save()
        return redirect(data)
    else:
        return render(request,'home.html')
    
    
def viewdata(request):
    x=Data.objects.all()
    return render(request,'view.html',{'data':x})

def delete(request,id):
    x=Data.objects.get(id=id)
    x.delete()
    return redirect(viewdata)

def edit(request,id):
    x=Data.objects.get(id=id)
    if request.method=='POST':
        
        x.Name=request.POST['name']
        x.Age=request.POST['age']
        x.Address=request.POST['address']
        x.save()
        return redirect(viewdata)
    else:     
        return render (request,'editpage.html',{'data':x})

        
        
    
