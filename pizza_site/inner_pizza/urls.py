from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('more_pizza', views.another_req, name="more_piz"),
    path('detail/<int:topping_id>/', views.detail, name="topping_detail"),
    path('', views.main_page, name="main"),
    # path('my_endpoint', views.my_function)
]