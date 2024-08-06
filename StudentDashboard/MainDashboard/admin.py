from django.contrib import admin
from .models import Category,UserDetails,Type,Mode,UpcomingCompanyDetails
# Register your models here.


admin.site.register(UserDetails)
admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Mode)
admin.site.register(UpcomingCompanyDetails)