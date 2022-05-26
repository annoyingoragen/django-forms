from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('order/',views.order,name='order'),
     path('pizzas/',views.pizzas,name='pizzas'),
     path('order/<int>',views.pizzas,name='pizzas'),
]