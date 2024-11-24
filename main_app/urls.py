from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('app/<slug:slug>', views.App_details_view, name='app_detail'),
    path('service/<slug:slug>', views.Service_details_view, name='Service_detail'),
]
