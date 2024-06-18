from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from .models import BookCategory, Book
from .forms import BookCategoryForm, BookForm
from django.db.models import Sum # type: ignore

# Book Category Views
def book_category_list(request):
    categories = BookCategory.objects.all()
    return render(request, 'books/book_category_list.html', {'categories': categories})

def book_category_create(request):
    if request.method == 'POST':
        form = BookCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_category_list')
    else:
        form = BookCategoryForm()
    return render(request, 'books/book_category_form.html', {'form': form})

def book_category_update(request, pk):
    category = get_object_or_404(BookCategory, pk=pk)
    if request.method == 'POST':
        form = BookCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('book_category_list')
    else:
        form = BookCategoryForm(instance=category)
    return render(request, 'books/book_category_form.html', {'form': form})

def book_category_delete(request, pk):
    category = get_object_or_404(BookCategory, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('book_category_list')
    return render(request, 'books/book_category_confirm_delete.html', {'category': category})

# Book Views
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})

def distribution_expenses_report(request):
    categories = BookCategory.objects.all()
    report_data = []
    for category in categories:
        total_expenses = Book.objects.filter(category=category).aggregate(Sum('distribution_expense'))['distribution_expense__sum']
        report_data.append({'category': category.name, 'total_expenses': total_expenses})

    return render(request, 'books/distribution_expenses_report.html', {'report_data': report_data})

def index(request):
    return render(request, 'index.html')
