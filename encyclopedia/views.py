from django.http import HttpResponse
from django.shortcuts import render

from . import util

from random import choice

from . import md_converter


from django import forms
#from django.http import HttpResponseRedirect
#from django.urls import reverse

class NewPage(forms.Form):
    title = forms.CharField (widget=forms.TextInput (attrs={'placeholder':'Enter title'}))
    content = forms.CharField (widget=forms.Textarea (attrs={'placeholder':'Enter content here\nAs markdown reference:\n#Heading\n**Bold**'}))

class EditForm(forms.Form):
    title = forms.CharField (widget=forms.TextInput)
    content = forms.CharField (widget=forms.Textarea)

class SearchForm(forms.Form):
    search = forms.CharField(label="Search",required= False, widget= forms.TextInput (attrs={'placeholder':'Search Encyclopedia'}))


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
    if request.method== "POST":
    # si existe post
        form = NewPage(request.POST)
        # tomar la info y guardar en fomulario
        if form.is_valid():
        # controlo si el formulario esta bien (server-side)
            title = form.cleaned_data["title"]
            # separo cada variable del formulario
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return entry_page(request, title)
            #return render(request, "encyclopedia/wiki.html", {"title": util.get_entry(title)})
        else:
           # return entry_page(request( util.save_entry(title, content)))
           # muestro el formulario con los campos completado
            return render(request, "encyclopedia/new_page.html", {"form": form
            })
    else:
        # si no existe post muestro el formulario vacio
        return render(request, "encyclopedia/new_page.html", {"form": NewPage()
        })
    

def edit_page(request, title):
    if request.method== "POST":
        edit = EditForm(request.POST)
        if edit.is_valid():
            title = edit.cleaned_data["title"]
            content = edit.cleaned_data["content"]
            #return render(request, "encyclopedia/new_page.html", {"form": form})
            util.save_entry(title, content)
    else:
        #return render(request, "encyclopedia/new_page.html", {"form": NewPage()})
        edit = EditForm({"title": title, "content": util.get_entry(title)})
        return render(request, "encyclopedia/edit.html", {"form": edit, "edit": edit})
    

def search(request,title):
    #search = SearchForm(request.POST or None)      
    #if request.method == "POST" and search.is_valid():
    if request.method == "POST":
        search = SearchForm(request.POST)
        if search.is_valid():
            search = search.cleaned_data["search"]
            #entries = util.list_entries()
            entry = util.get_entry(title)
        else:
            if search in entry:
                return render(request, "encyclopedia/wiki.html",{"search":search})
    else:
        #return HttpResponseRedirect("wiki:index")
        return render(request, "encyclopedia/wiki.html",{"search":SearchForm()})
    


'''def search(request):
    #search = SearchForm(request.POST or None)      
    #if request.method == "POST" and search.is_valid():
    if request.method == "POST":
        search = SearchForm(request.POST)
        if search.is_valid():
            search = search.cleaned_data["search"]
            return render(request, "encyclopedia/wiki.html",{"search":search})
    else:
        return render(request, "encyclopedia/wiki.html",{"search":SearchForm()})'''



'''def new_page(request):
    if request.method== "POST":
        form = NewPage(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if title == util.get_entry(title):
                print("An entry named:{title} already exists")
            

            else:
                util.save_entry(title, content)
                #return HttpResponseRedirect(reverse("wiki:wiki"))
                return entry_page(request, title)
                #return render(request, "encyclopedia/wiki.html", {"title": util.get_entry(title)})

        else:
           # return entry_page(request( util.save_entry(title, content)))
           #print("An entry named:{title} already exists")
            return render(request, "encyclopedia/new_page.html", {"form": form
            })
    else:
        return render(request, "encyclopedia/new_page.html", {"form": NewPage()
        })'''


            
'''return render(request, "encyclopedia/wiki.html",
    {"title": util.get_entry(title)})'''



'''def edit_page(request, title):
    if request.method== "POST":
        edit = EditForm(request.POST)
        if edit.is_valid():
            title = edit.cleaned_data["title"]
            content = edit.cleaned_data["content"]
            #return render(request, "encyclopedia/new_page.html", {"form": form})
            util.save_entry(title, content)
    else:
        #return render(request, "encyclopedia/new_page.html", {"form": NewPage()})
        edit = EditForm({"title": title, "content": util.get_entry(title)})
        return render(request, "encyclopedia/edit.html", {"form": edit, "edit": edit})'''