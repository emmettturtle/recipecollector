from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('recipes/', views.recipes_index, name='index'),
    path('recipes/<int:recipe_id>/', views.recipes_detail, name='detail'),
    path('recipes/create/', views.RecipeCreate.as_view(), name='recipes_create'),
    path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipes_update'),
    path('recipes/<int:pk>/delete', views.RecipeDelete.as_view(), name='recipes_delete'),
    path('recipes/<int:recipe_id>/add_comment/', views.add_comment, name='add_comment'),
    path('ingredients/create/', views.IngredientCreate.as_view(), name='ingredients_create'),
    path('ingredients/', views.IngredientList.as_view(), name='ingredients_index'),
    path('ingredients/<int:pk>/', views.IngredientDetail.as_view(), name='ingredients_detail'),
    path('ingredients/<int:pk>/update/', views.IngredientUpdate.as_view(), name='ingredients_update'),
    path('ingredients/<int:pk>/delete/', views.IngredientDelete.as_view(), name='ingredients_delete'),
    path('recipes/<int:recipe_id>/assoc_ingredient/<int:ingredient_id>', views.assoc_ingredient, name='assoc_ingredient'),
    path('recipes/<int:recipe_id>/remove_ingredient/<int:ingredient_id>', views.remove_ingredient, name='remove_ingredient'),

]