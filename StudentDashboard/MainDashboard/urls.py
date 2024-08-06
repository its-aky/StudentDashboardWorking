from django.urls import path
from . import views

app_name = 'dashboard' 

urlpatterns = [
    path('',views.index,name="MainDashboard"),
    path('dashboard/add_details',views.add_details,name="add_details"),
]