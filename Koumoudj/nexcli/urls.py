from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ticket/<str:client_type>/', views.ticket, name='ticket'),
    path('caisse/', views.caisse, name='caisse'),
    path('show/', views.show, name='show'),
    path('start/', views.start, name='start'),
]