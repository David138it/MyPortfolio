from django.contrib import admin
from .models import *
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'place', 'begin', 'scan', 'is_published')
    list_display_links = ('id', 'place')
    search_fields = ('title', 'progress')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'begin')
    prepopulated_fields = {"slug": ("place",)}
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Category, CategoryAdmin)