from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_skills, name='show_skills'),
]
