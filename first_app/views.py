from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    tv_shows_list={"tv_shows":{'Game of Thrones':'9.3','Blacklist': '8','Suits': '8.5','The Witcher': '8.5'}}
    return render(request,'first_app/index.html',context=tv_shows_list)

def home(request):
    return HttpResponse("Welcome to the Home page!")

def educative(request):
    return HttpResponse("Welcome to the Educative page")

def show_age(request, age):
    return HttpResponse("I am % s years old." % age)