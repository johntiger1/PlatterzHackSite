from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Topping
# Create your views here.

class IndexView(generic.ListView):
    template_name='inner_pizza/index.html'
    context_object_name = 'list_of_toppings'

    #this is if you want to set it once...
    #queryset=Topping.objects.all()

    # this is the new name
    def get_queryset(self):
        return Topping.objects.order_by('?')

    # this is the old legacy name
    def get_query_set(self):
        return Topping.objects.order_by('?')


class DetailView(generic.DetailView):
    model = Topping
    template_name = 'inner_pizza/detail.html'

class ResultsView(generic.DetailView):
    model = Topping
    template_name = 'inner_pizza/results.html'

def vote(request, topping_id):
    topping = get_object_or_404(Topping, pk=topping_id)

    # check that the dict is ok, or at least do a TryGetValue call

    if (request.POST['choice'] == "Like"):
        topping.topping_upvotes +=1
    elif (request.POST['choice'] == "Dislike"):
        topping.topping_downvotes +=1
    topping.save()

    return HttpResponseRedirect(reverse('inner_pizza:results', args=(topping_id,)))
