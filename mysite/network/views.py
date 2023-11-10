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
        for query in cloudlog:
            objects.append(query)
        return objects
