from django.shortcuts import render
from django.http import HttpResponse
import requests
API_KEY = '2fb6ad7da7864ce29a8c3ad78c913d92'

# Create your views here.

def home(request):
    country = request.GET.get('country')

    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    context = {
        'articles' : articles
    }

    return render(request, "home.html", context)