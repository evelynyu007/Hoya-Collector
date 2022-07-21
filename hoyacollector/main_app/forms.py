from django.forms import ModelForm
from .models import Cultivation

class CultivationForm(ModelForm):
  class Meta:
    model = Cultivation
    fields = ['date', 'care']