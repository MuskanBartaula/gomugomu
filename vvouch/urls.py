from os import name
from django.contrib import staticfiles
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-category', views.add_category, name='add-category'),
    path('add-subcategory', views.add_subcategory, name='add-subcategory'),
    path('add-archivo', views.add_archivo, name='add-archivo'),
    path('get-subcategory', views.get_subcategory, name='get-subcategory'),
    path('edit-category', views.edit_category, name='edit-category'),
    path('edit-subcategory', views.edit_subcategory, name='edit-subcategory'),
    path('edit-archivo', views.edit_archivo, name='edit-archivo'),
    path('edit-archivo-category-files', views.edit_archivo_category_files, name='edit-archivo-category-files'),
    path('delete-category', views.delete_category, name='delete-category'),
    path('delete-subcategory', views.delete_subcategory, name='delete-subcategory'),
    path('delete-category-files', views.delete_category_files, name='delete-category-files'),
    path('delete-subcategory-files', views.delete_subcategory_files, name='delete-subcategory-files'),
    path('get-subcategory-permission', views.get_subcategory_permission, name='get-subcategory-permission'),
    path('get_edit_subcategory_permission', views.get_edit_subcategory_permission, name='get_edit_subcategory_permission'),
    path('edit_permissions_in_subcategories', views.edit_permissions_in_subcategories, name='edit_permissions_in_subcategories'),
    path('data-json',views.data_json, name="data-json"),

    path('file/move/', views.handle_dragged_file, name="handle_dragged_file"),
    path('categories/order/', views.categories_order, name="categories_order"),
]

urlpatterns += staticfiles_urlpatterns()
