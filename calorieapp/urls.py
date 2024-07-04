from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_food_item, name='add_food_item'),
    path('delete/<int:item_id>/', views.delete_food_item, name='delete_food_item'),
    path('reset/', views.reset_calories, name='reset_calories'),
]