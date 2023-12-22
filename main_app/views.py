from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from datetime import date
from .models import Recipe
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
    comment_form = CommentForm()
    return render(request, 'recipes/detail.html', {
        'recipe': recipe,
        'comment_form': comment_form
    })

class RecipeCreate(CreateView):
    model = Recipe
    fields = '__all__'

class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['ingredients', 'directions']

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

