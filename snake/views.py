#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Family, Snake

class HomeView(ListView):
    model = Snake
    template_name = 'snake/list.html'
    context_object_name = "snakes"
    queryset = Snake.objects.order_by('family__name')

class DetailsView(DetailView):
    model = Snake
    template_name = 'snake/details.html'
    context_object_name = "snake"
    query_pk_and_slug = True
