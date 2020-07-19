from django.shortcuts import render
from app import forms
# Create your views here.
def home(request):
    form = forms.CrudForm()
    return render(request,'home.html',{'form':form})