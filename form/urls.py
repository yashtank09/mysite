from django.urls import path
from .views import form_example

app_name = 'form'
urlpatterns = [
    path('example/', form_example),
]