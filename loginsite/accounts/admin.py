from django.contrib import admin
from django.contrib.auth.models import Group


# Register your models here.
from .models import SecurityQuestion

class SecurityQuestionAdmin(admin.ModelAdmin):
    fields = ['securityquestion', 'active', 'startdate','enddate', 'lastmodifyby']
    list_display = ('securityquestion', 'active', 'startdate', 'lastmodifyby')
#    search_fields = ('securityquestion')
    ordering = ('securityquestion',)
    list_filter = ('active', 'startdate',)

admin.site.site_header = 'LogInSite Admin Dashboard'
admin.site.register(SecurityQuestion, SecurityQuestionAdmin)

#admin.site.register(Customer)
#admin.site.register(Product)
#admin.site.register(Tag)
#admin.site.register(Order)