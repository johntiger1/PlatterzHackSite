from django.urls import path

from . import views
app_name = "inner_pizza"
urlpatterns = [
    path('index', views.index, name='index'),
    path('more_pizza', views.another_req, name="more_piz"),
    path('<int:topping_id>/', views.detail, name="topping_detail"),
    path('<int:topping_id>/vote/', views.vote, name='vote'),
    path('<int:topping_id>/results/', views.results, name="results"),
    path('', views.main_page, name="main"),
    # path('my_endpoint', views.my_function)
]