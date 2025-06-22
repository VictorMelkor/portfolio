from django import forms
from .models import Message

class ContactForm(forms.ModelForm):
    
    class Meta():
        model = Message

        fields = ['name', 'email', 'subject', 'message']
        
        labels = {
            'name': 'Nome',
            'email': 'e-mail',
            'subject': 'Assunto',
            'message': 'Mensagem',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Digite seu nome completo',
                'class': 'form-control', 
                'aria-label': 'Nome Completo'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'exemplo@seuemail.com',
                'class': 'form-control',
                'required': True,
                'aria-label': 'exemplo@seuemail.com'
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Sobre o que você quer falar?',
                'class': 'form-control',
                'required': True,
                'aria-label': 'Sobre o que você quer falar?'
            }),
            'message': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Escreva sua mensagem aqui...',
                'class': 'form-control',
                'required': True,
                'aria-label': 'Escreva sua mensagem aqui...'
            }),
        }
