from django.http import HttpResponse
from django.shortcuts import render

from . import util

from random import choice

from . import md_converter


from django import forms

class NewPage(forms.Form):
    title = forms.CharField (widget=forms.TextInput (attrs={'placeholder':'Enter title'}))
    content = forms.CharField (widget=forms.Textarea (attrs={'placeholder':'Enter content here\nAs markdown reference:\n#Heading\n**Bold**'}))


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

'''def wiki(request, name):
    return render(request, "encyclopedia/wiki.html", {
        "name": name.capitalize()
    })'''


'''
def entry_page(request, title):
    return render(request, "encyclopedia/wiki.html",
    {"title": util.get_entry(title)})
    '''

def entry_page(request, title):
     entry_md=util.get_entry(title)
     html = md_converter.to_html(entry_md)
     print(html)
     return render(request, "encyclopedia/wiki.html",{"title": html})

'''
TypeError at /wiki/css
get_entry() missing 1 required positional argument: 'title

needed to add the word title inside()
'''

def random_page(request):
    return entry_page(request,choice( util.list_entries()))

def new_page(request):
    #if request.method== "POST":
        form = NewPage(request.POST)
        #if form.is_valid():
           # return entry_page(request( util.save_entry(title, content)))'''
        return render(request, "encyclopedia/new_page.html", {
                "form": form})
            
'''return render(request, "encyclopedia/wiki.html",
    {"title": util.get_entry(title)})'''