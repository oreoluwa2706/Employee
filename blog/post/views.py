from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse("cohort 13")


def greet(request):
    return HttpResponse("Good morning")


def helloo(request):
    return render(request, 'hello.html')


def money(request):
    return HttpResponse("Godii bless me with money π π§³ πΌ ποΈ π§ π€²πΌπ€²πΌπ€²πΌπ€²πΌπ€²πΌπ€²πΌπ«’")
