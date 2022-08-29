from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from . import models

# Create your views here.
# 
# class IndexView(TemplateView):
#     template_name = "index.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['content01'] = 'dynamic data'
#         return context
# 

class IndexView(TemplateView):
    template_name = "index.html"

class SchoolListView(ListView):
    context_object_name = "schools"
    model = models.School
    # by default this returns a list with the name of the model School and lowercases it and adds _list , example: school_list

class SchoolDetailView(DetailView):
    context_object_name = "school_detail"
    model = models.School
    template_name = "basicapp/school_detail.html"
    # by default it returns the model name School and lowercases it , example: school

class SchoolCreateView(CreateView):
    fields = ("name", "principal", "location")
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ("name", "principal")
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basicapp:list")
