from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('create/', views.create),
    path('confirmation/', views.confirmation),
    path('read/<int:id>/',views.read),
    path('update/<int:id>/',views.update),
    path('traitementupdate/<int:id>/',views.traitementupdate)
]