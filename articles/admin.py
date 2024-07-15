from django.contrib import admin

# Register your models here.
from .models import Article

# admin.site.register(Article)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'author',)
    date_hierarchy = 'published'
    search_fields = ('title', 'description', )