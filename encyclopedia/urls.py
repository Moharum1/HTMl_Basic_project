from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("entry/<str:name>", views.title, name="names"),
    path("search",views.Search,name="Query"),
    path("newPage",views.Createpage,name="newPage"),
    path("swaPage",views.swapage,name="swaPage"),
    path("edit/<str:name>",views.Edit,name="Edit"),
    path("Random",views.Random , name="Random")
]
