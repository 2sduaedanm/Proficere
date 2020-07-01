from django.contrib import admin
from django.contrib.auth.models import Group


# Register your models here.
from .models import *

class SecurityQuestionAdmin(admin.ModelAdmin):
    fields = ['securityquestion', 'active', 'startdate','enddate', 'lastmodifyby']
    list_display = ('securityquestion', 'active', 'startdate', 'lastmodifyby', 'lastmodifydate')
#    search_fields = ('securityquestion')
    ordering = ('securityquestion',)
    list_filter = ('active', 'startdate', 'lastmodifydate',)
    
class UserProfileAdmin(admin.ModelAdmin):
    fields = ['user', 'birthdate', 'active', 'startdate', 'enddate', 'lastmodifyby']
    list_display = ('user', 'birthdate', 'active', 'startdate', 'lastmodifyby', 'lastmodifydate')
    ordering = ('user',)
    list_filter = ('active', 'startdate', 'lastmodifydate',)

admin.site.site_header = 'LogInSite Admin Dashboard'
admin.site.register(SecurityQuestion, SecurityQuestionAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

#admin.site.register(Customer)
#admin.site.register(Product)
#admin.site.register(Tag)
#admin.site.register(Order)