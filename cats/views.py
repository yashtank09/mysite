from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Breed, Cat

# Create your views here.
class CatList(LoginRequiredMixin, View):
    def get(self, req):
        breed = Breed.objects.all().count()
        cat = Cat.objects.all()

        ctx = {'breed_count': breed, 'cat_list':cat}
        return render(req, 'cats/cat_list.html', ctx)

class BreedView(LoginRequiredMixin, View):
    def get(self, req):
        breed = Breed.objects.all()
        ctx = {'breed_list':breed}
        return render(req, 'cats/breed_list.html', ctx)


class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

# Cat views
class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')