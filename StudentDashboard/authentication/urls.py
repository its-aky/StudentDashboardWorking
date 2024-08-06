from .views import RegisView,UsernameValidationView,EmailValidationView,VerificationView,LoginView,LogoutView

from django.urls import path
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('register',RegisView.as_view(),name="register"),
    path('login',LoginView.as_view(),name="login"),
    path('logout',LogoutView.as_view(),name="logout"),
    path('validate-username',csrf_exempt(UsernameValidationView.as_view()),name="ValidateUserName"),
    path('validate-email',csrf_exempt(EmailValidationView.as_view()),name="ValidateEmail"),
    path('activate/<uid>/<token>',VerificationView.as_view(),name="activate"),#Notice how parameters are passed 
    
]
