from django.urls import path
from .views import view_all, delete_recipe, recipe_details, update_recipe, create_recipe

urlpatterns = [
    path('home/',view_all),
    path('recipe_details/<int:recipe_id>', recipe_details, name='recipe_details'),
    path('create_recipe/', create_recipe),
    path('delete_recipe/', delete_recipe),
    path('update_recipe/', update_recipe),
]