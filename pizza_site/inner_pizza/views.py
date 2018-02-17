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

# def index(request):
#     return HttpResponse("inner pizza ")
#
# def another_req(request):
#     return HttpResponse("more pizza stuff")
#


# def main_page(request):
#     # string_content = "the main page for inner_pizza. We currently have the following" \
#     #                  "toppings in the db\n\n"
#     # string_content+=str(Topping.objects.get(pk=1))
#
#     list_of_toppings = Topping.objects.all()
#     template = loader.get_template("inner_pizza/index.html")
#     context = {
#     'list_of_toppings' : list_of_toppings,
#
#     }
#     return HttpResponse(template.render(context,request))

def vote(request, topping_id):
    topping = get_object_or_404(Topping, pk=topping_id)

    # check that the dict is ok, or at least do a TryGetValue call

    if (request.POST['choice'] == "Like"):
        topping.topping_upvotes +=1
    elif (request.POST['choice'] == "Dislike"):
        topping.topping_downvotes +=1
    topping.save()

    return HttpResponseRedirect(reverse('inner_pizza:results', args=(topping_id,)))

#
# def results(request, topping_id):
#     try:
#         topping_obj = Topping.objects.get(pk=topping_id)
#     except Topping.DoesNotExist:
#         raise Http404("Topping does not exist")
#     return render(request, 'inner_pizza/results.html', {'topping': topping_obj})
#
#
# def detail(request, topping_id):
#     try:
#         topping_obj = Topping.objects.get(pk=topping_id)
#     except Topping.DoesNotExist:
#         raise Http404("Topping does not exist")
#     return render(request, 'inner_pizza/detail.html', {'topping': topping_obj})
#     # return HttpResponse("you're looking at %s topping" % topping_id)
