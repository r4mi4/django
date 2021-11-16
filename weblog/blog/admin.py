from django.contrib import admin
from .models import Article


# Register your models here.
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('title', 'writer', 'published')
# admin.site.register(Article, ArticleAdmin)

# two way customizing admin panel :)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'published', 'status')
    list_filter = ('status', 'title', 'writer')
    search_fields = ('title', 'body')
    raw_id_fields = ('writer',)
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('status',)
