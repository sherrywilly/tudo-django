from django import forms
from app.views import home

class CrudForm(forms.ModelForm):
    
    class Meta:
        model = Crud
        fields = '__all__'

