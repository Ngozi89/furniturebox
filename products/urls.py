from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_furnitures, name='furnitures'),
    path('<furniture_id>', views.furniture_detail, name='furniture_detail'),
]