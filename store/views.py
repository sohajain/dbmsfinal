from django.shortcuts import render
from .models import Book #, Cart, BookOrder

# Create your views here.
def index(request):
    return render (request, 'template.html')
def store(request):
    count = Book.objects.all()
    context = {
        'count': count,
    }
    return render(request, 'store.html',context)