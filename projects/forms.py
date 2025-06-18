from django import forms
from .models import Project

class FormProject(forms.ModelForm):
    
    class Meta():
        model = Project
        fields = ['title', 'description', 'tech_stack', 'url', 'image', 'is_featured']

        labels = {
            'title': 'Nome do Projeto',
            'description': 'Descrição', 
            'tech_stack': 'Tecnologias', 
            'url': 'URL do Projeto', 
            'image': 'Imagem do Projeto', 
            'is_featured': 'É Destaque'
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Nome do Projeto',
                'class': 'form-control', 
                'autofocus': True,
                'aria-label': 'Nome do Projeto'
                }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Descrição do Projeto',
                'class': 'form-control',
                'aria-label': 'Descrição do Projeto'
                }),
            'tech_stack': forms.TextInput(attrs={
                'placeholder': 'Ex: Django, React, PostgreSQL',
                'class': 'form-control',
                'aria-label': 'Ex: Django, React, PostgreSQL'
                }),
            'url': forms.URLInput(attrs={
                'placeholder': 'https://exemplo.com/projeto',
                'class': 'form-control',
                'aria-label': 'https://exemplo.com/projeto'
                }),            
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'aria-label': 'Imagem do projeto'
            }),
            'is_featured': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'aria-label': 'Marcar como destaque'
            }),

        }

