from django.urls import path

from .views import myview

app_name = 'home'
urlpatterns = [
    path('hello/', myview, name='myView'),
]