
from django import forms
from .models import BlogModel

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['title' , 'desc']

        
        labels = {
            'title' : 'Enter Blog Model',
            'desc' : 'Enter Blog Description'
        }

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'desc' : forms.Textarea(attrs={'class':'form-control'})
        }

        