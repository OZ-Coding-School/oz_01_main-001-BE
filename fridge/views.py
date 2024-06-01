from django.shortcuts import render, redirect
from django.contrib.auth import logout
import json
from django.http import JsonResponse
from .models import Ingredient

def fridge_main(request):
    if not request.user.is_authenticated:
        return redirect('/users/login/')

    ingredients = Ingredient.objects.all()
    context = {
        'ingredients': ingredients
    }

    return render(request, 'fridge/fridge_main.html', context)

def add_ingredient(request):
    if request.method == 'POST':
        data = request.POST
        ingredient_name = data.get('ingredient_name')
        ingredient_type = data.get('ingredient_type')
        expiration_date = data.get('expiration_date')

        ingredient = Ingredient.objects.create(
            ingredient_name=ingredient_name,
            ingredient_type=ingredient_type,
            expiration_date=expiration_date
        )

        return JsonResponse({'success': True, 'ingredient_id': ingredient.id})
    return JsonResponse({'success': False}, status=400)

