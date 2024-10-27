from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('edu/', views.initiatives, name='initiatives'),
    path('edu/pears/', views.pears, name='pears'),
]
