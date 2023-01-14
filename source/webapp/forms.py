from django import forms
from django.forms import widgets
from webapp.models import CATEGORY_CHOICES, Product, Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'user', 'rating', 'moderated']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'picture']
