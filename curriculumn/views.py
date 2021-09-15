from django.shortcuts import render
from django.views.generic import (TemplateView,DetailView,FormView,ListView)
from .models import (Standard,Subject,Lesson)
# Create your views here.
class StandardListView(ListView):
    context_object_name='standards'
    model=Standard
    template_name='curriculumn/standard_list_view.html'

class SubjectListView(DetailView):
    context_object_name='standards'
    model=Standard
    template_name='curriculumn/subject_list_view.html'