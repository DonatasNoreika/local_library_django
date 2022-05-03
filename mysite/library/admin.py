from django.contrib import admin

# Register your models here.
from .models import (Book,
                     BookInstance,
                     Genre,
                     Author)

admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Author)
