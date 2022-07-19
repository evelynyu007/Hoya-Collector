from django.shortcuts import render

# Create your views here.
# Add the following import
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Hoya:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, color, scent):
    self.name = name
    self.color = color
    self.scent = scent


hoya = [
  Hoya('Lolo', 'white', 'sweet'),
  Hoya('Sachi', 'black', 'chocoloate'),
  Hoya('Raven', 'pink', 'sweet')
]


# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

# Add new view
def hoya_index(request):
  return render(request, 'hoya/index.html', { 'hoya': hoya })