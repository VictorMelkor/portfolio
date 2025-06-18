from django.contrib import admin
from .models import Certificate, Skill, Experience, Education, Interest, ContactInfo, ResumeSettings

admin.site.register(Certificate)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Interest)
admin.site.register(ContactInfo)
admin.site.register(ResumeSettings)
