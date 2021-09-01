from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderListView.as_view()),
    path('<str:order_number>/', views.OrderDetailsView.as_view()),
]
