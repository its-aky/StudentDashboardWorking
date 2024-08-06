from django.shortcuts import render,redirect
import json
import os
from django.conf import settings
from .models import UserPreference
from django.contrib import messages


# For debugging
    # import pdb
    # pdb.set_trace() 
    
def index(request):
    branchs=[]
    file_path=os.path.join(settings.BASE_DIR , 'branch.json')
        
    with open(file_path,'r') as json_file:
        data=json.load(json_file)
            
        for key,value in data.items():
            branchs.append({"branch":key,"short":value})
        
    user_preference=None
    if UserPreference.objects.filter(user=request.user).exists()==True:
        user_preference=UserPreference.objects.get(user=request.user)
    
    if request.method=="GET":
        return render(request,'Preferences/index.html',{"branchs":branchs,'user_preference':user_preference})

    
    else:
        chosen_branch=request.POST['chosen_branch']
        if user_preference==None:
            UserPreference.objects.create(user=request.user,branch=chosen_branch)
            
        else:
            user_preference.branch=chosen_branch
            user_preference.save()

        messages.success(request,"Changes Saved")
        return render(request,'Preferences/index.html',{"branchs":branchs,'user_preference':user_preference})
        
    