from django.urls import path
from .import views
from kassa import views

app_name = 'kassa'

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.navbar, name='navbar'),
    path('hotels/', views.hotels, name='hotels'),
    path('termsofuse/', views.termsofuse, name='termsuofuse'),
    path('refund/', views.refund, name='refund'),
]