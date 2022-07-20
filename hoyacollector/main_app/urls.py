from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # route for Hoya index
  path('hoya/', views.hoya_index, name='index'),
  path('hoya/<int:hoya_id>/', views.hoya_detail, name='detail'),
  path('hoya/create/', views.HoyaCreate.as_view(), name ='hoya_create'),
  path('hoya/<int:pk>/update/', views.HoyaUpdate.as_view(), name='hoya_update'),
path('hoya/<int:pk>/delete/', views.HoyaDelete.as_view(), name='hoya_delete'),
]