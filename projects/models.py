from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    tech_stack = models.CharField(max_length=100)
    repo_url = models.URLField()
    demo_url = models.URLField(blank=True)  # opcional
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    is_featured = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
