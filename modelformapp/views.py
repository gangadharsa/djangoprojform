from django.shortcuts import render
from .forms import ProductForm
from .models import Product
from django.http import HttpResponse

# Create your views here.
def insert(request):
    if request.method == 'POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            p1=Product(pid=form.cleaned_data['pid'],
                       pname=form.cleaned_data['pname'],
                       pcost=form.cleaned_data['pcost'],
                       pmfdt=form.cleaned_data['pmfdt'],
                       pexpdt=form.cleaned_data['pexpdt'])
            p1.save()
        return HttpResponse("<html><body bgcolor=red><h1 color=white>data inserted successfully</h1></body></html>")
    else:
        form=ProductForm()
        return render(request,'input.html',{'form':form})



