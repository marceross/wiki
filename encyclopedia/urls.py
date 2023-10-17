from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("marce", views.marce, name="marce"),
    #path("wiki/<str:name>", views.wiki, name="wiki"),
    path("wiki/<str:title>", views.entry_page, name="entry_page"),
    # the directory where the file is configured in views.py
]


''' 
need to create this file in each app
if "" in first argument points to root


'''