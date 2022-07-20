from django.shortcuts import render

# Create your views here.
# Add the following import
from django.http import HttpResponse
from .models import Hoya
# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView



# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

# Add new view
def hoya_index(request):
  hoya = Hoya.objects.all()
  return render(request, 'hoya/index.html', { 'hoya': hoya })

def hoya_detail(request, hoya_id):
  hoya = Hoya.objects.get(id = hoya_id)
  return render(request, 'hoya/detail.html', { 'hoya': hoya })

class HoyaCreate(CreateView):
  model = Hoya
  fields = '__all__'

class HoyaUpdate(UpdateView):
  model = Hoya
  fields = '__all__'

class HoyaDelete(DeleteView):
  model = Hoya
  success_url='/hoya/'