from django.contrib import admin
from .models import AddBook, Author
# Register your models here.

admin.site.register(Author)

@admin.register(AddBook)
class AddBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )