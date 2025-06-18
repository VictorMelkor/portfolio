from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.ContactView.as_view(), name='contact'),
    path('thanks/', views.ContactSuccessView.as_view(), name='thanks'),
]