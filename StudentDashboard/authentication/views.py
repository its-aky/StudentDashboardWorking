from django.shortcuts import render,redirect
from django.views import View
from django.http import JsonResponse #server to website response
from django.contrib.auth.models import User

from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib import auth

#imports made to encode and decode the UID and token generation
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import token_generator
# JSON helps in passing data between frontend(website) and backend(server)
import json



# Renders a HTML page upon request
class RegisView(View):
   def get(self,request):
      return render(request,'authentication/Register.html')
   def post(self,request):
      #Steps: 1)Get User Data 2)Validate 3)Create a user account and set user as inactive 4)Send verification email
      
      #(1)
      
      username=request.POST['username']
      email=request.POST['email']
      password=request.POST['password']
      
      # When the password is too short then the username and email should be kept as same in the form field
      context={'FieldValues':request.POST}

      # (2)
      
      if not User.objects.filter(username=username).exists():
         if not User.objects.filter(email=email).exists():
            if len(password)<8:
               messages.error(request,"PASSWORD IS TOO SHORT")
               return render(request,'authentication/Register.html',context)
            
            
            # (3)
            
            user=User.objects.create_user(username=username,email=email)
            user.set_password(password)
            user.is_active=False
            user.save()
            
            #Token and UID steps->
            # 1)getting domain we are on
            # 2)relative url to verification
            # 3)Encode UID
            # 4)Token
            uid=urlsafe_base64_encode(force_bytes(user.pk))
            domain=get_current_site(request).domain
            link=reverse('activate',kwargs={'uid':uid,'token':token_generator.make_token(user)})
            print(domain)
            print(link)
            # reverse is a utility function used to generate URLs for Django views. It allows you to dynamically build a URL based on a named URL pattern defined in your Django project's URL configuration (urls.py)
            activate_url="http://"+domain+link
            
            EmailSubject="Activate your account"
            EmailBody="Hi "+user.username+" Please use the link below to activate your account\n" + activate_url
            email = EmailMessage(
               EmailSubject,
               EmailBody,
               "noreply@kohda.com",
               [email],

            )
            email.send(fail_silently=False)
            messages.success(request,"ACCOUNT CREATED SUCCESSFULLY")
            return render(request,'authentication/Register.html')
            
         
      return render(request,'authentication/Register.html')

# 
class UsernameValidationView(View):
    def post(self,request):
        data=json.loads(request.body) #whole data comes in request.body
        username=data['username']
        
        #checks
         
        #checking only alphanumeric username
        if not str(username).isalnum():
           return  JsonResponse({"Username_Error":"Username can only contain alphanumeric characters"},status=400)
 
        #checking redundant username 
        if User.objects.filter(username=username).exists():
           return  JsonResponse({"Username_Error":"Username is already taken"},status=400)
       
        return JsonResponse({"UsernameValid":True})
    
class EmailValidationView(View):
    def post(self,request):
        data=json.loads(request.body) #whole data comes in request.body
        email=data['email']
        
        #checks
        
        #Validating EmailID
        if not validate_email(email):
           return  JsonResponse({"Email_Error":"Invalid Email"},status=400)
 
        #checking redundant email 
        if User.objects.filter(email=email).exists():
           return  JsonResponse({"Email_Error":"Email is already taken"},status=400)
       
        return JsonResponse({"EmailValid":True})
     

class VerificationView(View):
   def get(self,request,uid,token):
      #
      try:
         id = force_str(urlsafe_base64_decode(uid))
         user = User.objects.get(pk=id)

         if not token_generator.check_token(user, token):
            return redirect('login'+'?message='+'Wrong Credentials')

         if user.is_active:
            return redirect('login'+'?message='+'User already activated')
         
         user.is_active = True
         user.save()

         messages.success(request,'ACCOUNT ACTIVATED SUCCESSFULLY')
         return redirect('login')
      
      except Exception as ex:
         pass

      return redirect('login')

# After verification this view will render the display
class LoginView(View):
   def get(self,request):
      return render(request,'authentication/Login.html')
   
   def post(self,request):
      
      username=request.POST['username']
      password=request.POST['password']
      
      if username and password:
         
         user=auth.authenticate(username=username,password=password)
         
         if user:
            if user.is_active:
               auth.login(request,user)
               messages.success(request,"Welcome "+ user.username + " ,You are now logged in")
               return redirect('dashboard:MainDashboard')
               
            messages.error(request,"User is not activated ,Please Check Your Email")
            return render(request,'authentication/Login.html')
         
         messages.error(request,"Invalid Credentials")
         return render(request,'authentication/Login.html')  
                  
               
      messages.error(request,"Please Fill All The Fields")
      return render(request,'authentication/Login.html')     
         
    
class LogoutView(View):
   def post(self,request):
      auth.logout(request)
      messages.success(request,"You have been logged Out")
      return redirect("login")