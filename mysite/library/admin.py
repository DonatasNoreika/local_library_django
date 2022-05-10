from django.contrib import admin

# Register your models here.
from .models import (Book,
                     BookInstance,
                     Genre,
                     Author)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0 # išjungia placeholder'ius
    readonly_fields = ('uuid',)
    can_delete = False

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'summary', 'display_genre')
    inlines = [BooksInstanceInline]


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'reader', 'due_back', 'uuid')
    list_filter = ('status', 'due_back')
    search_fields = ('uuid', 'book__title')
    list_editable = ('due_back', 'reader', 'status')

    fieldsets = (
        ('General', {'fields': ('uuid', 'book')}),
        ('Availability', {'fields': ('reader', 'status', 'due_back')}),
    )

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'display_books')

admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Genre)
admin.site.register(Author, AuthorAdmin)
