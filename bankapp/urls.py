from django.urls import path
from . import views

urlpatterns = [

    path('view_customers', views.view_customers, name="view_customers"),
    path('', views.home, name="home"),
    # path('/Customer_form', views.Customer_form, name="Customer_form"),
    path('details/<user_id>/', views.details, name='details'),
    path('transfer_money/<user_id>/', views.transfer_money, name="transfer_money"),
    path('add_money/<user_id>/<user>/', views.addMoney, name="add")
    # path('completed', views.completed, name="completed")
]
