from django.contrib import admin

from home.models import AudioAuthor, AudioCategory, Audiobook, Author, Category, Ebook

# Register your models here.
class EbookAdmin(admin.ModelAdmin):
    list_display = ('title','author','category',)
    list_filter = ('author','category',)
    search_fields = ('title',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Ebook,EbookAdmin)



class AudiobookAdmin(admin.ModelAdmin):
    list_display = ('title','author','category',)
    list_filter = ('author','category',)
    search_fields = ('title',)

class AudioCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

class AudioAuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

admin.site.register(AudioCategory,AudioCategoryAdmin)
admin.site.register(AudioAuthor,AudioAuthorAdmin)
admin.site.register(Audiobook,AudiobookAdmin)