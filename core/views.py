from django.views.generic.edit import CreateView
from contact.forms import ContactForm
from contact.models import Message
from projects.models import Project
from resume.models import Experience, Education, Certificate, Skill, Interest, ContactInfo, ResumeSettings


class HomeView(CreateView):
    model = Message
    form_class = ContactForm
    template_name = 'core/home.html'
    success_url = '/'  # <-- corrige a rolagem automática

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(is_featured=True)
        context['certificates'] = Certificate.objects.all()
        context['skills'] = Skill.objects.all()
        context['experiences'] = Experience.objects.all()
        context['educations'] = Education.objects.all()
        context['interest'] = Interest.objects.all()
        context['contact_info'] = ContactInfo.objects.all()  # nome da variável corrigido
        context['resume'] = ResumeSettings.objects.all()
        return context
