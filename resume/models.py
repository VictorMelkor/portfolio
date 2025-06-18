from django.db import models

class Certificate(models.Model):
    title = models.CharField(max_length=50)
    institution = models.CharField(max_length=50)
    issue_date = models.DateField()
    certificate_file = models.FileField(upload_to='certificates/', null=True, blank=True)
    url = models.URLField(blank=True)
    description = models.TextField(blank=True)


class Skill(models.Model):

    SKILL_CHOICES = [
        ('beginner', 'Iniciante'),
        ('intermediary', 'Intermediário'),
        ('advanced', 'Avançado'),
    ]

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    level = models.CharField(max_length=15, choices=SKILL_CHOICES, blank=True, null=True)
    icon = models.ImageField(upload_to='skills/icons/', blank=True, null=True)
    highlight = models.BooleanField(default=False)


class Experience(models.Model):
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    location = models.CharField(max_length=30)


class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=50)
    course_name = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True)


class Interest(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)


class ContactInfo(models.Model):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=14)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True)
    location = models.CharField(max_length=30)


class ResumeSettings(models.Model):
    resume_file = models.FileField(upload_to='resume/', null=True, blank=True)
    show_resume_download = models.BooleanField(default=True)
    show_contact_info = models.BooleanField(default=True)

