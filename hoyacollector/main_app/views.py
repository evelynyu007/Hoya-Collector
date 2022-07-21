from django.shortcuts import render, redirect

# Create your views here.
# Add the following import
from django.http import HttpResponse
from .models import Hoya, Planter
from .forms import CultivationForm
# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


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
  # Get the planters the hoya doesn't have...
  # First, create a list of the planter ids that the hoya DOES have
  id_list = hoya.planters.all().values_list('id')
  # Now we can query for planters whose ids are not in the list using exclude
  planters_hoya_doesnt_have = Planter.objects.exclude(id__in=id_list)
  # instatiate CultivationForm to be rendered in the template
  cultivation_form = CultivationForm()
  return render(request, 'hoya/detail.html', { 'hoya': hoya, 'cultivation_form': cultivation_form,
  'planters':planters_hoya_doesnt_have })

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
  fields = ['name', 'color', 'scent', 'img'] 

class HoyaUpdate(UpdateView):
  model = Hoya
  fields = '__all__'

class HoyaDelete(DeleteView):
  model = Hoya
  success_url='/hoya/'

class PlanterList(ListView):
  model = Planter 

class PlanterDetail(DetailView):
  model =Planter 

class PlanterCreate(CreateView):
  model =Planter 
  fields = '__all__'

class PlanterUpdate(UpdateView):
  model =Planter 
  fields = ['name', 'material']

class PlanterDelete(DeleteView):
  model =Planter 
  success_url = '/Planters/'


def assoc_planter(request, hoya_id, planter_id):
  Hoya.objects.get(id=hoya_id).planters.add(planter_id)
  return redirect('detail', hoya_id=hoya_id)