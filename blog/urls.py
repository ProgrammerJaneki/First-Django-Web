from django.urls import path
from . import views
from users import views as reg_views

urlpatterns = [
    path('', views.home, name ='blog-home'),
    path('about/', views.about, name ='blog-about'),
]