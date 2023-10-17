Wiki project
Done with visiting /wiki/TITLE
Understood urls.py from project and from app
Understood views.py
Understood routing
Started debuging, very helpfull







django-admin startproject mysite

mysite/
    manage.py
    mysite/
        __init__.py
        settings.py (EVERYTIME I CREATE A NEW APP ADD THE NEW APP)
        urls.py (ADD THE THE NEW PATH FOR THE NEW APP)
        asgi.py
        wsgi.py

ls
I see: mysite

py manage.py runserver
I see: Django's default page, this is a project
Can have multiple different apps

py mangage.py startapp myapp

myapp/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py

In myapp folder
create urls.py
create views.py

mysite folder
urls.py (FROM THE PROJECT)
This is the master url's file that says which other apps I can have access
urls.py mysite
path('wiki/', include("encyclopedia.urls"))

urls.py myapp
path("wiki/<str:name>", views.wiki, name="wiki"),

views.py
def wiki(request, name):
    return render(request, "encyclopedia/wiki.html", {
        "name": name.capitalize()
    })

So, basically we have to point...


https://docs.djangoproject.com/en/4.2/intro/tutorial01/



The outer **mysite/** root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
**manage.py**: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.
The inner **mysite/** directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).
**mysite/__init__.py**: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.
**mysite/settings.py**: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
**mysite/urls.py**: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.
**mysite/asgi.py**: An entry-point for ASGI-compatible web servers to serve your project. See How to deploy with ASGI for more details.
**mysite/wsgi.py**: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.







https://www.markdownguide.org/basic-syntax/
# Heading =<h1>
###### Heading =<h6>
*italic*
**bold**

* item \ to escape the.
* item
or
- item
or
+ item

1. item 1
2. item 2

[this is a link](https://link.com)


url or email into link
<hello@email.com>
<mysite.com>


Nested Blockquotes
> Some text text
>> Some more text inside

code `this is code`

***

