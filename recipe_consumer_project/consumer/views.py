from django.shortcuts import render
import requests

def recipe_list(request):
    api_url = "http://127.0.0.1:8000/recipes/"
    response = requests.get(api_url)
    recipes_data = response.json()  # assuming the API response is in JSON format
    return render(request, 'consumer/recipe_list.html', {'recipes_data': recipes_data})
