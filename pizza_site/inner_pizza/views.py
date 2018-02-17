from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Topping
# Create your views here.
def index(request):
    return HttpResponse("inner pizza ")

def another_req(request):
    return HttpResponse("more pizza stuff")

def main_page(request):
    # string_content = "the main page for inner_pizza. We currently have the following" \
    #                  "toppings in the db\n\n"
    # string_content+=str(Topping.objects.get(pk=1))

    list_of_toppings = Topping.objects.all()
    template = loader.get_template("inner_pizza/index.html")
    context = {
    'list_of_toppings' : list_of_toppings,

    }
    return HttpResponse(template.render(context,request))

def detail(request, topping_id):
    return HttpResponse("you're looking at %s topping" % topping_id)
