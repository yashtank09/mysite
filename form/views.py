from django.http import HttpResponse
from django.shortcuts import render
from .forms import BasicForm
# Create your views here.

# form view
def form_example(req):
    form = BasicForm()
    return HttpResponse(form.as_table())