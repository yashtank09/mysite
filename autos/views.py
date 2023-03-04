from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Make, Auto
from .forms import MakeForm

# Create your views here.
class Mainview(LoginRequiredMixin, View):
    def get(self, req):
        mc = Make.objects.all().count() # count of Makes
        al = Auto.objects.all()

        ctx = {'make_count': mc, 'auto_list': al}
        return render(req, 'autos/auto_list.html', ctx)

class MakeView(LoginRequiredMixin, View):
    def get(self, req):
        ml = Make.objects.all()
        ctx = {'make_list': ml}
        return render(req, 'autos/make_list.html', ctx)

# We use reverse_lazy() because we are in "Constructor attribute" flow that is run before urls.py is completely loaded
class MakeCreate(LoginRequiredMixin, View):
    template = 'autos/make_form.html'
    success_url = reverse_lazy('autos:all')

    def get(self, req):
        form = MakeForm(req.POST)
        ctx = {'form': form}
        return render(req, self.template, ctx)

    def post(self, req):
        form = MakeForm(req.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(req, self.template, ctx)

        make = form.save()
        return redirect(self.success_url)

# MakeUpdate has code to implement the get/post/validate/store flow
# AutoUpdate (below) is doing the same thing with no code
# and no form by extending UpdateView
class MakeUpdate(LoginRequiredMixin, View):
    model = Make
    success_url = reverse_lazy('autos:all')
    template = 'autos/make_form.html'

    def get(self, req, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=make)
        ctx = {'form': form}
        return render(req, self.template, ctx)

    def post(self, req, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=make)
        if not form.is_valid():
            ctx = {'form': form}
            return render(req, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class MakeDelete(LoginRequiredMixin, View):
    model = Make
    success_url = reverse_lazy('autos:all')
    template = 'autos/make_confirm_delete.html'

    def get(self, req, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=make)
        ctx = {'form': make}
        return render(req, self.template, ctx)

    def post(self, req, pk):
        make = get_object_or_404(self.model, pk=pk)
        make.delete()
        return redirect(self.success_url)

# Take the easy way out on the main table
# These views do not need a form because CreateView, UpdateView etc.
# Build a form object dynamically based on the fields
# value in the constructor attributes
class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')