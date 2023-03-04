from django.forms import ModelForm
from .models import Make

# creating a form class
class MakeForm(ModelForm):
    class Meta:
        model = Make
        fields = '__all__'