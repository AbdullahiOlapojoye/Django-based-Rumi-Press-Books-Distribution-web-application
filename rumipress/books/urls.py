from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.book_category_list, name='book_category_list'),
    path('categories/create/', views.book_category_create, name='book_category_create'),
    path('categories/update/<int:pk>/', views.book_category_update, name='book_category_update'),
    path('categories/delete/<int:pk>/', views.book_category_delete, name='book_category_delete'),
    path('books/', views.book_list, name='book_list'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/update/<int:pk>/', views.book_update, name='book_update'),
    path('books/delete/<int:pk>/', views.book_delete, name='book_delete'),
    path('report/', views.distribution_expenses_report, name='distribution_expenses_report'),
]
#urlpatterns += [
##    path('report/', views.distribution_expenses_report, name='distribution_expenses_report'),
#]
