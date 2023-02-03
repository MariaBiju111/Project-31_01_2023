from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def book(request):
    lst=['Book1','Book2', 'Book3','Book4', 'Book5']
    context={
        'book_list': lst,
    }
    return render(request,'book.html',context)

def book_detail(request,id):
    stg = f"This is book {id}'s detail page"
    context={
        "bid":stg
    }
    return render(request, 'book_detail.html',context)        

# Create your views here.
