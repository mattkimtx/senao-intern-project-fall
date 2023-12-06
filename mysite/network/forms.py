from django import forms

maxLength = 100

class SearchForm(forms.Form):
     search = forms.CharField(label="search", max_length=maxLength)
