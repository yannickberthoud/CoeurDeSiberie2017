from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Cat

class HomeView(ListView):
    model = Cat
    template_name = 'cat/list.html'
    context_object_name = "cats"

class DetailsView(DetailView):
    model = Cat
    template_name = 'cat/details.html'
    context_object_name = "cat"
    pk_url_kwarg = "cat_slug"
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True

def fiche(request):
    return render(request, 'cat/fiche.html')

def jut(request):
    return render(request, 'cat/jut.html')