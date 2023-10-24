from django.http import HttpResponseRedirect
# from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import TextLogs, Company

class IndexView(generic.ListView):
    template_name = "network/templates/mysite/index.html"

class SearchResultsView(generic.ListView):
    model = TextLogs
    # template_name = "network/search_results.html"

    # def get_queryset(self): 

        # query = self.request.GET.get("q")
        # object_list = TextLogs.objects.filter(
        #     Q(name__icontains=query) | Q(state__icontains=query)
        # )
        # return object_list