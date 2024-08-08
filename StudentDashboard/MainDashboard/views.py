from django.shortcuts import render,redirect
from .models import UpcomingCompanyDetails,Curriculum
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
import json
from django.db.models import Q
from django.http import JsonResponse
from UserPreferences.models import UserPreference

@login_required(login_url='/authentication/login')

def ajax_search(request):
    
    if request.method=="POST":
        search_str = json.loads(request.body).get('searchText')
        
        company_details = UpcomingCompanyDetails.objects.filter(  
            Q(name_of_company__icontains=search_str) |
            Q(year_of_passing__icontains=search_str) |
            Q(preferred_branch__icontains=search_str) |
            Q(type__icontains=search_str) |
            Q(mode__icontains=search_str) |
            Q(category__icontains=search_str)
        )
            

        data = company_details.values()
        return JsonResponse(list(data), safe=False)



def index(request):
    company_details=UpcomingCompanyDetails.objects.all()
    paginator = Paginator(company_details, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context={
        "company_details":company_details,
        'page_obj':page_obj,
    }
    return render(request,'MainDashboard/index.html',context)


def add_details(request):
    
    user_preference=None
    if UserPreference.objects.filter(user=request.user).exists()==True:
        user_preference=UserPreference.objects.get(user=request.user)
    
    subjects=[]
    if(user_preference):
        mixedbranch = user_preference.branch

        branch = mixedbranch.split('-')[1].strip()
        
        
        semester = user_preference.semester
        
        get_subjects=Curriculum.objects.filter(branch=branch,semester=semester).first()
        
        if get_subjects:
            subjects=[get_subjects.subject_one,
            get_subjects.subject_two,
            get_subjects.subject_three,
            get_subjects.subject_four,
            get_subjects.subject_five,
            get_subjects.subject_six]
            
       
    
    if request.method=="GET":
        return render(request,'MainDashboard/add_details.html',{"subjects":subjects})
    
    
            
    
