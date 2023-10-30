from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/", views.index, name="wiki"),
    path("wiki/<str:title>", views.entry_page, name="entry_page"),
    path("wiki/<str:title>", views.entry_page, name="link"),
    path("random/", views.random_page, name="random"),

    path("new_page/", views.new_page, name="new_page"),

    # the directory where the file is configured in views.py
]


''' 
need to create this file in each app
if "" in first argument points to root


'''