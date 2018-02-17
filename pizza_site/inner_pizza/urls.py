from django.urls import path

from . import views
app_name = "inner_pizza"
urlpatterns = [

    path('', views.IndexView.as_view(), name= 'main'),
    path('<int:pk>/', views.DetailView.as_view(), name='topping_detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    # path('index', views.index, name='index'),
    # path('more_pizza', views.another_req, name="more_piz"),
    # path('<int:topping_id>/', views.detail, name="topping_detail"),
    path('<int:topping_id>/vote/', views.vote, name='vote'),
    # path('<int:topping_id>/results/', views.results, name="results"),
    # path('', views.main_page, name="main"),
    # path('my_endpoint', views.my_function)
]