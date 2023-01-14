from django import forms
from django.forms import widgets
from webapp.models import CATEGORY_CHOICES, Product

#
# class SearchForm(forms.Form):
#     search = forms.CharField(max_length=50, required=False, label="Найти")
#

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'picture']