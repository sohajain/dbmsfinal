from django.shortcuts import render
from .models import Book #, Cart, BookOrder

# Create your views here.
def index(request):
    return render (request, 'template.html')
def store(request):
    count = Book.objects.all()
    context = {
        'count': count,
        'page':'welcome to mystery books!'
    }
    return render(request, 'base.html',context)