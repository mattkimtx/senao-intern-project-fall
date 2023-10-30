from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
# from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import TextLogs, Company
from .forms import SearchForm

# class IndexView(generic.ListView):
#     template_name = "network/templates/mysite/index.html"

#     def get_queryset(self): 

#         query = self.request.GET.get("q")
#         object_list = TextLogs.objects.filter(eventTitle__icontains=query)
#         return object_list

class IndexView(generic.ListView):
    model = TextLogs
    template_name = "network/index.html"
    queryset=TextLogs.objects.all()
    context_object_name = "posts"
    
class SearchResultsView(generic.ListView):
    model = TextLogs
    template_name = "network/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        query = self.request.GET.get('q')
        return TextLogs.objects.filter(eventTitle__icontains=query).order_by('-category')


def findEvent(request):
    # if this is a post request
    if request.method == "GET":
        # create a form with data from request
        form = SearchForm(request.POST)
        # check if valid
        if form.is_valid():
            # get the data
            query = form.cleaned_data["q"]
            search_query = form.get_results(query)
            # redirect to a new URL:
            return HttpResponseRedirect("/network/index.html")
    else:
        form = SearchForm()

    return render(request, "network/index.html", {"form": form})