from django.contrib import admin
from .models import Book #,BookOrder, Author, Cart
# Register your models here.
class BookAdmin(admin.ModelAdmin):
     list_display = ('title', 'price', 'stock')
admin.site.register(Book,BookAdmin)
