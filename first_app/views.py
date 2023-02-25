from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World!")

def home(request):
    return HttpResponse("Welcome to the Home page!")

def educative(request):
    return HttpResponse("Welcome to the Educative page")

def show_age(request, age):
    return HttpResponse("I am % s years old." % age)