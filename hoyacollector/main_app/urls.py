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
  path('hoya/<int:hoya_id>/add_cultivation/', views.add_cultivation, name='add_cultivation'),
  path('planters/', views.PlanterList.as_view(), name='planters_index'),
  path('planters/<int:pk>/', views.PlanterDetail.as_view(), name='planters_detail'),
  path('planters/create/', views.PlanterCreate.as_view(), name='planters_create'),
  path('planters/<int:pk>/update/', views.PlanterUpdate.as_view(), name='planters_update'),
  path('planters/<int:pk>/delete/', views.PlanterDelete.as_view(), name='planters_delete'),
  # associate a toy with a cat (M:M)
  path('hoya/<int:hoya_id>/assoc_planter/<int:planter_id>/', views.assoc_planter, name='assoc_planter'),
  # path('hoya/<int:hoya_id>/add_photo/', views.add_photo, name='add_photo'),
]