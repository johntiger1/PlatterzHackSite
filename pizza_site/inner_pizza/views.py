from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("inner pizza ")

def another_req(request):
    return HttpResponse("more pizza stuff")

def main_page(request):
    return HttpResponse("the main page for inner_pizza")