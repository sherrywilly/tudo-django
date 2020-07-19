from django.shortcuts import render,redirect
from app.forms import CrudForm
from app.models import Crud
# Create your views here.

def home(request):
    form = CrudForm()
    cruds = Crud.objects.all()
    if request.method == 'POST':
       form = CrudForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('home')
    return render(request,'home.html',{'form':form, 'cruds':cruds})

def update(request, crud_id):
    crud = Crud.objects.get(id=crud_id)
    form =CrudForm(instance=crud)
    if request.method =='POST':
        form =CrudForm(request.POST,instance=crud)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'update.html',{'form':form,'crud':crud})

def delete(request,crud_id):
     if request.method == 'POST':
         Crud.objects.get(id=crud_id).delete()
         return redirect('home')
