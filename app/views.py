
from django.shortcuts import render
import requests
#from django.http import HttpResponse
#from django.template import loader
#from django.template.loader import get_template


# Create your views here.


def quote(request):
    response= requests.get('https://dummyjson.com/quotes/random')
    quote_data = response.json()

    context = {
        'quote': quote_data['quote'],
        'author': quote_data['author']
    }
    return render(request, 'index.html',context)   
   # template = loader.get_template('quote.html')

  #  return HttpResponse(template.render())
