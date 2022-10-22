from django.http import HttpResponse
from django.shortcuts import render

def index(request):
 return render(request, "index.html")

def about(request):
    # 1. return HttpResponse('Tis is my first page (Это моя первая страница)')
    # 2. return render(request, "about.html") # при вызове "about" открываем страницу "about.html"
    # 3. return render(request, "about.html", {'gretting': 'hello'})  # передадим на страницу словарь {'gretting' : 'hello'}
    a = 5**2 #  произведем некоторые вычисления
    return render(request, "about.html", {'NumberSquare': a})
def home(request):
    return HttpResponse('This is my home')