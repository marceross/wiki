from django.http import HttpResponse
from django.shortcuts import render

from . import util

from random import choice


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

'''def wiki(request, name):
    return render(request, "encyclopedia/wiki.html", {
        "name": name.capitalize()
    })'''

def entry_page(request, title):
    return render(request, "encyclopedia/wiki.html",
    {"title": util.get_entry(title)})
'''
TypeError at /wiki/css
get_entry() missing 1 required positional argument: 'title

needed to add the word title inside()
'''

def random_page(request):
    return entry_page(request,choice( util.list_entries()))