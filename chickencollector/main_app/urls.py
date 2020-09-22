from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('chickens/', views.chickens_index, name='index'),
    path('chickens/<int:chicken_id>/', views.chickens_detail, name='detail'),
    path('chickens/create/', views.ChickenCreate.as_view(), name='chickens_create'),
    path('chickens/<int:pk>/update/', views.ChickenUpdate.as_view(), name='chickens_update'),
    path('chickens/<int:pk>/delete/', views.ChickenDelete.as_view(), name='chickens_delete'),
    path('chickens/<int:chicken_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('chickens/<int:chicken_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('chickens/<int:chicken_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]