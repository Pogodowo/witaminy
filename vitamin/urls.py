from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home,name='home'),
    path('formJson/<str:skl>/', views.formJson, name='formJson'),
    path('dodajskl/', views.dodajsklJson, name='dodajsklJson'),
    path('aktualizujTabela/', views.aktualizujTabela, name='aktualizujTabela'),
    path('delSkl/<str:id>/', views.delSkl, name='delSkl'),
]