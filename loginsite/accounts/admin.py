from django.contrib import admin
from django.contrib.auth.models import Group


# Register your models here.
from .models import *

class SecurityQuestionAdmin(admin.ModelAdmin):
    fields = ['securityquestion', 'active', 'startdate','enddate']
    list_display = ('securityquestion', 'active', 'startdate', 'lastmodifydate',)
#    search_fields = ('securityquestion')
    ordering = ('id',)
    list_filter = ('active', 'startdate', 'lastmodifydate',)
    
class UserProfileAdmin(admin.ModelAdmin):
    fields = ['user', 'birthdate', 'securityquestion01', 'securityanswer01', 'active', 'startdate', 'enddate']
    list_display = ('user', 'birthdate', 'active', 'startdate', 'lastmodifydate')
    ordering = ('user',)
    list_filter = ('active', 'startdate', 'lastmodifydate',)
    
class AddressTypeAdmin(admin.ModelAdmin):
    fields = ['addresstype', 'active', 'startdate', 'enddate']
    list_display = ('addresstype', 'active', 'startdate', 'lastmodifydate')
    ordering = ('id',)
    list_filter = ('active', 'startdate', 'lastmodifydate',)
    
class CountryAdmin(admin.ModelAdmin):
    fields = ['country', 'active', 'startdate', 'enddate']
    list_display = ('country', 'active', 'startdate', 'lastmodifydate')
    ordering = ('id',)
    list_filter = ('active', 'startdate', 'lastmodifydate',)
    
class StateAdmin(admin.ModelAdmin):
    fields = ['country', 'state', 'statename', 'active', 'startdate', 'enddate']
    list_display = ('state', 'statename','country',  'active', 'startdate', 'lastmodifydate')
    ordering = ('country', 'state',)
    list_filter = ('active', 'startdate', 'lastmodifydate',)
    
class AddressAdmin(admin.ModelAdmin):
    fields = ['addresstype', 'country', 'addressline01', 'addressline02', 'addressline03', 'city', 'state', 'postalcode', 'active', 'startdate', 'enddate']
    list_display = ('addresstype', 'country', 'city', 'state', 'addressline01', 'active', 'startdate', 'lastmodifydate')
    ordering = ('addresstype', 'country', 'city', 'state', 'addressline01',)
    list_filter = ('active', 'startdate', 'lastmodifydate',)
    
class PhoneTypeAdmin(admin.ModelAdmin):
    fields = ['phonetype', 'active', 'startdate', 'enddate']
    list_display = ('phonetype', 'active', 'startdate', 'lastmodifydate')
    ordering = ('id',)
    list_filter = ('active', 'startdate', 'lastmodifydate',)
    
class CountryExchangeAdmin(admin.ModelAdmin):
    fields = ['country', 'countryexchange', 'active', 'startdate', 'enddate']
    list_display = ('country', 'countryexchange', 'active', 'startdate', 'lastmodifydate')
    ordering = ('countryexchange',)
    list_filter = ('active', 'startdate', 'lastmodifydate',)
    
class PhoneAdmin(admin.ModelAdmin):
    fields = ['phonetype', 'countryexchange', 'phoneno', 'active', 'startdate', 'enddate']
    list_display = ('phonetype', 'countryexchange', 'phoneno', 'active', 'startdate', 'lastmodifydate')
    ordering = ('id',)
    list_filter = ('active', 'startdate', 'lastmodifydate',)
    
class EmailTypeAdmin(admin.ModelAdmin):
    fields = ['emailtype', 'active', 'startdate', 'enddate']
    list_display = ('emailtype', 'active', 'startdate', 'lastmodifydate')
    ordering = ('id',)
    list_filter = ('active', 'startdate', 'lastmodifydate',)
    
class EmailAddressAdmin(admin.ModelAdmin):
    fields = ['emailtype', 'emailaddress', 'active', 'startdate', 'enddate']
    list_display = ('emailtype', 'emailaddress', 'active', 'startdate', 'lastmodifydate')
    ordering = ('emailtype', 'emailaddress',)
    list_filter = ('active', 'startdate', 'lastmodifydate',)


admin.site.site_header = 'LogInSite Admin Dashboard'
admin.site.register(SecurityQuestion, SecurityQuestionAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(AddressType, AddressTypeAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(PhoneType, PhoneTypeAdmin)
admin.site.register(CountryExchange, CountryExchangeAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(EmailType, EmailTypeAdmin)
admin.site.register(EmailAddress, EmailAddressAdmin)

#admin.site.register(Customer)
#admin.site.register(Product)
#admin.site.register(Tag)
#admin.site.register(Order)