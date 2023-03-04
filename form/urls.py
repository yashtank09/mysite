from django.urls import path
from .views import form_example

app_name = 'forms'
urlpatterns = [
    path('', form_example, name='forms'),
]