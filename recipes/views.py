from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe

# Create your views here.
@login_required(login_url="/authentication/login/")
def view_all(request):
    user = request.user
    recipes = Recipe.objects.filter(user=user)
    return render(request,'view_all.html', {'recipes': recipes})

@login_required(login_url="/authentication/login/")
def recipe_details(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, user=request.user)
    steps = recipe.steps.splitlines()
    ingredients = recipe.ingredients.splitlines()
    return render(request,'details.html', {'recipe': recipe,'steps': steps, 'ingredients': ingredients})
@login_required(login_url="/authentication/login/")
def create_recipe(request):
    pass

@login_required(login_url="/authentication/login/")
def update_recipe(request):
    pass

@login_required(login_url="/authentication/login/")

def delete_recipe(request):
    pass