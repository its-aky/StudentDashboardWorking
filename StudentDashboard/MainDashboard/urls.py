from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'dashboard' 

urlpatterns = [
    path('',views.index,name="MainDashboard"),
    path('add_details',views.add_details,name="add_details"),
    path('search',csrf_exempt(views.ajax_search),name="ajax_search"),
]