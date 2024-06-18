from django import forms
from .models import BookCategory, Book

class BookCategoryForm(forms.ModelForm):
    class Meta:
        model = BookCategory
        fields = ['name']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'subtitle', 'authors', 'publisher', 'published_date', 'category', 'distribution_expense']
