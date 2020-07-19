from django import forms
from app.models import Crud

class CrudForm(forms.ModelForm):
    
    class Meta:
        model = Crud
        fields = '__all__'

