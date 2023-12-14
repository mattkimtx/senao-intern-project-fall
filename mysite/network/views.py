from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .services import get_all_rows
from .models import TextLogs, Company
from .forms import SearchForm
from utils import get_db_handle
from pymongo import MongoClient

def my_view(request):
    try:
        db_handle, client = get_db_handle('cloud6_intern', '35.165.140.135', '27017', 'jino', 'G&Qw5fccQKZ8gdvv')
        print(client.list_database_names())
        all_data = {}

        for col_name in db_handle.list_collection_names():
            print(1)
            collection = db_handle[col_name]
            print(2)
            data = list(collection.find({}))
            print(3)
            all_data[col_name] = data
            print(4)
        print(5)
        print(all_data)
        # Close the MongoDB connection
        client.close()
        print(6)

                # Render the template with the data
        return render(request, 'network/data_display.html', {'all_data': all_data})

    except Exception as e:
        # Handle exceptions (e.g., connection errors)
        return render(request, 'network/error.html', {'error_message': str(e)})

    # return render(request, 'network/data_display.html')

# # queryset is not limited to single row, it will be used to display all rows in the database
# class IndexView(generic.ListView):
#     # cloudlog is a list of dictionaries, each dictionary holds data for each event
#     cloudlog = get_all_rows("cloudlog")
#     # identify queryset
#     queryset = cloudlog
#     template_name = "network/index.html" 
#     context_object_name = "posts"
    
# # limit queryset to search box input, will show only rows that match the search query
# class SearchResultsView(generic.ListView):
#     cloudlog = get_all_rows("cloudlog")
#     queryset = cloudlog
#     template_name = "network/index.html"
#     context_object_name = "posts"

#     def get_queryset(self):
#         objects = []
#         cloudlog = get_all_rows("cloudlog")
#         query = self.request.GET.get('q')
#         # search for events that match in cloud log. Only matches beginning from first character in string, will not identify matches in part of the string.
#         for event in cloudlog:
#             value = event.get("eventTitle")
#             if query in value or query == value:
#                 objects.append(event)
#         return objects