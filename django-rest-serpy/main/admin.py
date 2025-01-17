from django.contrib import admin
from .models import Category, Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']


admin.site.register(Category)
admin.site.register(Book, BookAdmin)