from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import BookCategory, Book

class BookResource(resources.ModelResource):
    class Meta:
        model = Book

class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource

admin.site.register(BookCategory)
admin.site.register(Book, BookAdmin)
