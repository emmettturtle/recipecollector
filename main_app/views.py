from django.shortcuts import render

# Create your views here.
recipes = [
    {'title': 'Chicken Shawarma', 'ingredients': ['chicken thighs', 'shawarma marinade'], 'directions': 'Marinade chicken and then grill'},
    {'title': 'Finger Lime Tzatziki', 'ingredients': ['finger limes', 'tzatziki'], 'directions': 'Mix fingerlimes with tzatziki.'},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def recipes_index(request):
    return render(request, 'recipes/index.html', {
        'recipes': recipes
    })