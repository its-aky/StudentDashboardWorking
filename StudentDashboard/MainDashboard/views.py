from django.shortcuts import render,redirect
from .models import Category,UserDetails,Type,Mode,UpcomingCompanyDetails
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
@login_required(login_url='/authentication/login')
# Create your views here.
def index(request):
    company_details=UpcomingCompanyDetails.objects.all()
    expenses = UpcomingCompanyDetails.objects.filter(owner=request.user)
    paginator = Paginator(expenses, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context={
        "company_details":company_details,
    }
    return render(request,'MainDashboard/index.html',context)


def add_details(request):
    categories=Category.objects.all()
    types=Type.objects.all()
    modes=Mode.objects.all()

    
    context={
        "categories":categories,
        "types":types,
        "modes":modes,
        "values":request.POST,
    }
    
    if request.method=="GET":
        return render(request,'MainDashboard/add_details.html',context)
    
    if request.method=="POST":
        
        name=request.POST['name']
        year=request.POST['year']
        branch=request.POST['branch']
        type=request.POST['type']
        mode=request.POST['mode']
        category=request.POST['category']
        
        if not name:
            messages.error(request,"Name is required")
            return render(request,'MainDashboard/add_details.html',context)
        
        if not year:
            messages.error(request,"Year is required")
            return render(request,'MainDashboard/add_details.html',context)
        
        if not branch:
            messages.error(request,"Branch is required")
            return render(request,'MainDashboard/add_details.html',context)
        
        
        UserDetails.objects.create(student=request.user,name=name,year=year,branch=branch,type=type,mode=mode,category=category)
        messages.success(request,"USER DETAILS ADDED SUCCESSFULLY")
        return redirect('dashboard:MainDashboard')
            
    
