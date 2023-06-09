from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('create/', views.create),
    path('confirmation/', views.confirmation),
    path('read/<int:id>/',views.read),
    path('update/<int:id>/',views.update),
    path('traitementupdate/<int:id>/',views.traitementupdate),
    path('delete/<int:id>/' ,views.delete),

    #categorie Parc :
    path('parc/createparc/', views.createparc),
    path('parc/confirmationparc/', views.confirmationparc),
    path('parc/readparc/<int:id>/', views.readparc),
    path('parc/updateparc/<int:id>/', views.updateparc),
    path('parc/traitementupdateparc/<int:id>/', views.traitementupdateparc),
    path('parc/deleteparc/<int:id>/', views.deleteparc)

]