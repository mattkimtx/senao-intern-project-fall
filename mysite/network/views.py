from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
# from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .services import get_all_rows

from .models import TextLogs, Company
from .forms import SearchForm

class IndexView(generic.ListView):
    cloudlog = get_all_rows("cloudlog") # don't need queryset because cloudlog is a dictionary (i think, not 100% positive)
    queryset = cloudlog
    template_name = "network/index.html" 
    context_object_name = "posts"

    
class SearchResultsView(generic.ListView):
    cloudlog = get_all_rows("cloudlog")
    queryset = cloudlog
    template_name = "network/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        objects = []
        cloudlog = get_all_rows("cloudlog")
        query = self.request.GET.get('q')
        for event in cloudlog:
            objects.append(event)
        return objects

# def searchEvents(request):
#     if request.method == "POST":
#         searched = request.POST['q']

# def findEvent(request):
#     # if this is a post request
#     if request.method == "GET":
#         # create a form with data from request
#         form = SearchForm(request.POST)
#         # check if valid
#         if form.is_valid():
#             # get the data
#             query = form.cleaned_data["q"]
#             search_query = form.get_results(query)
#             # redirect to a new URL:
#             return HttpResponseRedirect("/network/index.html")
#     else:
#         form = SearchForm()

#     return render(request, "network/index.html", {"form": form})