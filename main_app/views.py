from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from datetime import date
from .models import Recipe, Ingredient
from .forms import CommentForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def recipes_index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', {
        'recipes': recipes
    })

def recipes_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    id_list = recipe.ingredients.all().values_list('id')
    not_in_recipe = Ingredient.objects.exclude(id__in=id_list)
    comment_form = CommentForm()
    return render(request, 'recipes/detail.html', {
        'recipe': recipe,
        'comment_form': comment_form,
        'ingredients': not_in_recipe
    })

class RecipeCreate(CreateView):
    model = Recipe
    fields = ['title', 'directions']

class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['directions']

class RecipeDelete(DeleteView):
    model = Recipe
    success_url = '/recipes'

def add_comment(request, recipe_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.recipe_id = recipe_id
        new_comment.date = date.today()
        new_comment.save()
    return redirect('detail', recipe_id=recipe_id)

class IngredientCreate(CreateView):
    model = Ingredient
    fields = '__all__'

class IngredientList(ListView):
    model = Ingredient

class IngredientDetail(DetailView):
    model = Ingredient

class IngredientUpdate(UpdateView):
    model = Ingredient
    fields = ['name']

class IngredientDelete(DeleteView):
    model = Ingredient
    success_url = '/ingredients'

def assoc_ingredient(request, recipe_id, ingredient_id):
    Recipe.objects.get(id=recipe_id).ingredients.add(ingredient_id)
    return redirect('detail', recipe_id=recipe_id)

def remove_ingredient(request, recipe_id, ingredient_id):
    Recipe.objects.get(id=recipe_id).ingredients.remove(ingredient_id)
    return redirect('detail', recipe_id=recipe_id)
