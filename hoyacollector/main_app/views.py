from django.shortcuts import render, redirect

# Create your views here.
# Add the following import
from django.http import HttpResponse
from .models import Hoya
from .forms import CultivationForm
# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView



# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Add new view
def hoya_index(request):
  hoya = Hoya.objects.all()
  return render(request, 'hoya/index.html', { 'hoya': hoya })

def hoya_detail(request, hoya_id):
  hoya = Hoya.objects.get(id = hoya_id)
  # instatiate CultivationForm to be rendered in the template
  cultivation_form = CultivationForm()
  return render(request, 'hoya/detail.html', { 'hoya': hoya, 'cultivation_form': cultivation_form })

def add_cultivation(request, hoya_id):
  # create a ModelForm instance using the data in request.POST
  form = CultivationForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_cultivation = form.save(commit=False)
    new_cultivation.hoya_id = hoya_id
    new_cultivation.save()
  return redirect('detail', hoya_id=hoya_id)

class HoyaCreate(CreateView):
  model = Hoya
  fields = '__all__'

class HoyaUpdate(UpdateView):
  model = Hoya
  fields = '__all__'

class HoyaDelete(DeleteView):
  model = Hoya
  success_url='/hoya/'