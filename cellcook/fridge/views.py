from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Ingredient, Menu, IngredientMenuMapping, Recipe

@login_required
def fridge_main(request):
    """
    냉장고 재료 리스트를 보여주는 뷰
    """
    ingredients = Ingredient.objects.all()
    return render(request, 'fridge-main.html', {'ingredients': ingredients})

@login_required
def ingredient_create(request):
    if request.method == 'POST':
        ingredient_id = request.POST.get('ingredient_id')
        ingredient_name = request.POST.get('ingredient_name')
        ingredient_type = request.POST.get('ingredient_type')
        expiration_date = request.POST.get('expiration_date')

        ingredient = Ingredient.objects.create(
            ingredient_id=ingredient_id,
            user=request.user,
            ingredient_name=ingredient_name,
            ingredient_type=ingredient_type,
            expiration_date=expiration_date
        )

        return redirect('fridge-main')
    return render(request, 'ingredient.html')

@login_required
def menu_create(request):
    if request.method == 'POST':
        menu_name = request.POST.get('menu_name')
        menu_description = request.POST.get('menu_description')

        menu = Menu(
            menu_name=menu_name,
            menu_description=menu_description
        )
        menu.save()
        return redirect('menu_list')
    return render(request, 'menu.html')

@login_required
def ingredient_menu_mapping_create(request):
    if request.method == 'POST':
        ingredient_id = request.POST.get('ingredient_id')
        menu_id = request.POST.get('menu_id')

        mapping = IngredientMenuMapping(
            ingredient_id=ingredient_id,
            menu_id=menu_id
        )
        mapping.save()
        return redirect('ingredient_menu_mapping_list')
    return render(request, 'ingredient_menu_mapping.html')

@login_required
def recipe_create(request):
    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')

        recipe = Recipe(
            recipe_name=recipe_name,
            recipe_description=recipe_description
        )
        recipe.save()
        return redirect('recipe_list')
    return render(request, 'recipe.html')
