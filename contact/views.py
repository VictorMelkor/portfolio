from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .models import Message
from .forms import ContactForm

class ContactView(CreateView):
    model = Message
    form_class = ContactForm
    template_name = 'contact/contact_form.html'
    success_url = reverse_lazy('contact:thanks')

class ContactSuccessView(TemplateView):
    template_name = 'contact/thanks.html'

