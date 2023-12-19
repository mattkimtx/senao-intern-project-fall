from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .services import get_all_rows
from .models import TextLogs, Company
from .forms import SearchForm
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from django.conf import settings

load_dotenv()

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

# This is to return the data from the database to the html page
def my_view(request):
    try:
        secret = os.environ.get("CONNECTION_STRING")
        client = MongoClient(host=secret, directconnection=True)
        print(client)
        all_data = []
        all_data.append(client.list_database_names())
        # Close the MongoDB connection
        client.close()

                # Render the template with the data
        return render(request, 'network/data_display.html', {'all_data' : all_data})
    
    except Exception as e:
        # Handle exceptions (e.g., connection errors)
        raise Http404("No data found")
        # return render(request, 'network/error.html', {'error_message': str(e)})

def mongo_dbs(request):

    try:
        # Connect to the MongoDB server
        secret = os.environ.get("CONNECTION_STRING")
        client = MongoClient(host=secret, directconnection=True)
        all_db = client.list_database_names()
        all_data = []
        database = ""
        collection = ""

        # list of all possible queries
        dbQuery = request.GET.get('q1')
        clQuery = request.GET.get('q2')

        # Query database, collection, or file
        # shows all collections in database
        if dbQuery:
            for db in all_db:
                if db in dbQuery or dbQuery == db:
                    database = db
                    collectionDB = client[db]
                    all_data = collectionDB.list_collection_names()
        # shows all documents in collection
        if clQuery:
            for db in all_db:
                for cl in client[db].list_collection_names():
                    if cl in clQuery or clQuery == cl:
                        collection = cl
                        # query by name
                        documentCL = client[db][cl].find({}, {"_id": 1, "name": 1})
                        for doc in documentCL:
                            all_data.append(doc)
        # close mongoDB connection
        client.close()

        return render(request, 'network/data_display.html', {'database' : database,
                                                             'collection' : collection,
                                                             'all_data' : all_data,
                                                             })
    
    except Exception as e:
        # Handle exceptions (e.g., connection errors)
        raise Http404("No data found")
        # return render(request, 'network/error.html', {'error_message': str(e)})


def crud(request):
    try:
        secret = os.environ.get("CONNECTION_STRING")
        client = MongoClient(host=secret, directconnection=True)
        inserted = []

        input = request.GET.get('q')
        update = request.GET.get('update1')
        delete = request.GET.get('delete1')

        if input:
            doc = input.split(" ")
            # database is first part
            database = doc[0]
            # collection is second part
            collection = client[database][doc[1]]
            # insert document into collection
            collection.insert_one({"name": doc[2], "age": doc[3], "ID": doc[4]})
            # variable to return to website
            inserted = doc
        
        elif update:
            doc = update.split(" ")
            # database is first part
            database = doc[0]
            # collection is second part
            collection = client[database][doc[1]]
            # update one document in collection
            collection.update_one( 
                {
                    "query": {"ID": doc[4]},
                    "update": {"$set": {"name": doc[2], "age": doc[3]}},
                    }
                )
            # variable to return to website
            inserted = doc
        
        elif delete:
            doc = delete.split(" ")
            # database is first part
            database = doc[0]
            # collection is second part
            collection = client[database][doc[1]]
            # delete document from collection
            collection.delete_one( {"name": doc[2], "age": doc[3], "ID": doc[4]} )
            # variable to return to website
            inserted = doc

        client.close()

        return render(request, 'network/crud.html', {'inserted' : inserted,})
    except Exception as e:
        # Handle exceptions (e.g., connection errors)
        # raise Http404("No data found")
        return render(request, 'network/error.html', {'error_message': str(e)})
