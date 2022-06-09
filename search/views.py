from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from .form import  SearchForm
# Create your views here.
from bs4 import BeautifulSoup

import requests

from googlesearch import search
import urllib
from bs4 import BeautifulSoup
import csv


try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 



def index(request):
    form = SearchForm()
    if request.method=='POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = dict(form.cleaned_data)
            # to search
            query = data['text']
            response = HttpResponse(
                content_type='text/csv'
            )
            response['Content-Disposition'] = 'attachment; filename="urls.csv"'


            writer = csv.writer(response)
            
            for j in search(query, tld="com", num=10, stop=data['count'], pause=2):
                print(j)



                writer.writerow([j])

            return response

        else:
            print(dict(form.errors))

    else:
        return render(request,'index.html',{"form":form})

