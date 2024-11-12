from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm

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
    if request.method == 'POST':
        form  = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('recipes:view_all')
    form = RecipeForm()
    return render(request,'add_recipe.html', {'recipe_form': form})

@login_required(login_url="/authentication/login/")
def update_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, user=request.user)
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
            return redirect('recipes:view_all')
    else:
        form = RecipeForm(instance=recipe)
        return render(request,'edit_recipe.html', {'recipe_form': form,'recipe': recipe})

@login_required(login_url="/authentication/login/")
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, user=request.user)
    recipe.delete()
    return redirect('recipes:view_all')