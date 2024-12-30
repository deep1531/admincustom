from django.contrib import admin
from .models import Order, Product


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image')  # Columns displayed in the admin list view
    prepopulated_fields = {'slug': ('name',)}  # Auto-fill slug from name
    search_fields = ('name',)  # Searchable fields
    list_filter = ('name',)  # Filters for the admin sidebar


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'stock')  # Columns displayed in the admin list view
    prepopulated_fields = {'slug': ('name',)}  # Auto-fill slug from name
    search_fields = ('name', 'description')  # Searchable fields
    list_filter = ('name',)  # Filters for the admin sidebar
    ordering = ('-stock', 'name')  # Default ordering
    