import random

from django.http import HttpResponse
from django.shortcuts import render
import difflib
from django.db.models import Q

from . import util

# Default web page
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

################################################################################################

# the entry loading page
def title(request,name):
    if name in util.list_entries():
        return render(request,"encyclopedia/title.html",{
            "entry": util.get_entry(name),
            "Content" : name,
        })
    else:
        return HttpResponse("This Entry Doesn't exist")

################################################################################################

# the Search page
def Search(request):
    Query = request.GET.get('q')

    if Query in util.list_entries(): # this is a dict and we will get the query from it
        return render(request,"encyclopedia/title.html",{
            "entry" : util.get_entry(Query)
        })
    else :
        nearest=difflib.get_close_matches(Query,util.list_entries())
        return render(request, "encyclopedia/Search.html",{
            "nearest" : nearest ,
            "leng" : len(nearest)
        })

##################################################################################################

# Create page button press
def Createpage(request):
    return render(request,"encyclopedia/CreatePage.html")

##################################################################################################

# Moving into New page after creating a new markdown file
def swapage(request):
    Pagetitle = request.GET.get('title')
    PageContent = request.GET.get("Container")

    if Pagetitle in util.list_entries():
        return render(request, "encyclopedia/CreatePage.html" , {
            "error": 0,
        })
    else:
        util.save_entry(Pagetitle,PageContent)
        return render(request, "encyclopedia/title.html", {
            "entry": util.get_entry(Pagetitle),
            "Content" : Pagetitle
        })

#################################################################################################

# TO edit an existing Markup page
def Edit(request,name):
    return render(request, "encyclopedia/Edit.html",{
        "Content" : util.LoadText(name)
    })

##############################################################################################
def Random(request):
    page=random.choice(util.list_entries())
    return render(request,"encyclopedia/title.html",{
            "entry": util.get_entry(page),
            "Content" : page,
    })