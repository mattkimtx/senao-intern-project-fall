from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .services import get_all_rows
from .models import TextLogs, Company
from .forms import SearchForm
from .mongo_db import get_database
from dotenv import load_dotenv

load_dotenv()

def my_view(request):
    db = get_database()
    collection = db.cloud6_intern

    # Perform operations, e.g., find, insert
    data = collection.find_one({"key": "value"})

    # Process and return response
    return render(request, 'data_display.html', {'data': data})

# queryset is not limited to single row, it will be used to display all rows in the database
class IndexView(generic.ListView):
    # cloudlog is a list of dictionaries, each dictionary holds data for each event
    cloudlog = get_all_rows("cloudlog")
    # identify queryset
    queryset = cloudlog
    template_name = "network/index.html" 
    context_object_name = "posts"
    
# limit queryset to search box input, will show only rows that match the search query
class SearchResultsView(generic.ListView):
    cloudlog = get_all_rows("cloudlog")
    queryset = cloudlog
    template_name = "network/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        objects = []
        cloudlog = get_all_rows("cloudlog")
        query = self.request.GET.get('q')
        # search for events that match in cloud log. Only matches beginning from first character in string, will not identify matches in part of the string.
        for event in cloudlog:
            value = event.get("eventTitle")
            if query in value or query == value:
                objects.append(event)
        return objects