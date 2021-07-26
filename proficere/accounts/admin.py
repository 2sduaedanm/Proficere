from django.contrib import admin
from django.contrib.auth.models import Group


# Register your models here.
from .models import *

@admin.register(SecurityQuestion)
class SecurityQuestionAdmin(admin.ModelAdmin):
    fields = ['securityquestion', 'active', 'startdate','enddate']
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'created_by'):
            instance.created_by = request.user
        instance.lastmodifyby = request.user
        instance.save()
        form.save_m2m()
        return instance
    list_display = ('securityquestion', 'active', 'startdate', 'lastmodifydate',)
#    search_fields = ('securityquestion')
    ordering = ('id',)
    list_filter = ('active', 'startdate', 'lastmodifydate',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    fields = ['user', 'birthdate', 'userphoto', 'securityquestion01', 'securityanswer01', 'active', 'startdate', 'enddate']
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'created_by'):
            instance.created_by = request.user
        instance.lastmodifyby = request.user
        instance.save()
        form.save_m2m()
        return instance
    list_display = ('user', 'birthdate', 'userphoto', 'active', 'startdate', 'lastmodifydate')
    ordering = ('user',)
    list_filter = ('active', 'startdate', 'lastmodifydate',)

@admin.register(AddressType)
class AddressTypeAdmin(admin.ModelAdmin):
    fields = ['addresstype', 'active', 'startdate', 'enddate']
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'created_by'):
            instance.created_by = request.user
        instance.lastmodifyby = request.user
        instance.save()
        form.save_m2m()
        return instance
    list_display = ('addresstype', 'active', 'startdate', 'lastmodifydate')
    ordering = ('id',)
    list_filter = ('active', 'startdate', 'lastmodifydate',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    fields = ['country', 'active', 'startdate', 'enddate']
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'created_by'):
            instance.created_by = request.user
        instance.lastmodifyby = request.user
        instance.save()
        form.save_m2m()
        return instance
    list_display = ('country', 'active', 'startdate', 'lastmodifydate')
    ordering = ('id',)
    list_filter = ('active', 'startdate', 'lastmodifydate',)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    fields = ['country', 'state', 'statename', 'active', 'startdate', 'enddate']
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'created_by'):
            instance.created_by = request.user
        instance.lastmodifyby = request.user
        instance.save()
        form.save_m2m()
        return instance
    list_display = ('state', 'statename','country',  'active', 'startdate', 'lastmodifydate')
    ordering = ('country', 'state',)
    list_filter = ('active', 'startdate', 'lastmodifydate',)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    fields = ['addresstype', 'country', 'addressline01', 'addressline02', 'addressline03', 'city', 'state', 'postalcode', 'active', 'startdate', 'enddate']
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'created_by'):
            instance.created_by = request.user
        instance.lastmodifyby = request.user
        instance.save()
        form.save_m2m()
        return instance
    list_display = ('addresstype', 'country', 'city', 'state', 'addressline01', 'active', 'startdate', 'lastmodifydate')
    ordering = ('addresstype', 'country', 'city', 'state', 'addressline01',)
    list_filter = ('active', 'startdate', 'lastmodifydate',)

@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    fields = ['user', 'address', 'primaryuseraddress', 'active', 'startdate', 'enddate']
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'created_by'):
            instance.created_by = request.user
        instance.lastmodifyby = request.user
        instance.save()
        form.save_m2m()
        return instance
    list_display = ('user', 'address', 'primaryuseraddress', 'active', 'startdate', 'lastmodifydate')
    ordering = ('user', 'primaryuseraddress', 'address',)
    list_filter = ('active', 'startdate', 'lastmodifydate',)

@admin.register(PhoneType)
class PhoneTypeAdmin(admin.ModelAdmin):
    fields = ['phonetype', 'active', 'startdate', 'enddate']
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'created_by'):
            instance.created_by = request.user
        instance.lastmodifyby = request.user
        instance.save()
        form.save_m2m()
        return instance
    list_display = ('phonetype', 'active', 'startdate', 'lastmodifydate')
    ordering = ('id',)
    list_filter = ('active', 'startdate', 'lastmodifydate',)

@admin.register(CountryExchange)
class CountryExchangeAdmin(admin.ModelAdmin):
    fields = ['country', 'countryexchange', 'active', 'startdate', 'enddate']
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'created_by'):
            instance.created_by = request.user
        instance.lastmodifyby = request.user
        instance.save()
        form.save_m2m()
        return instance
    list_display = ('country', 'countryexchange', 'active', 'startdate', 'lastmodifydate')
    ordering = ('countryexchange',)
    list_filter = ('active', 'startdate', 'lastmodifydate',)

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    fields = ['phonetype', 'countryexchange', 'phoneno', 'active', 'startdate', 'enddate']
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'created_by'):
            instance.created_by = request.user
        instance.lastmodifyby = request.user
        instance.save()
        form.save_m2m()
        return instance
    list_display = ('phonetype', 'countryexchange', 'phoneno', 'active', 'startdate', 'lastmodifydate')
    ordering = ('id',)
    list_filter = ('active', 'startdate', 'lastmodifydate',)

@admin.register(UserPhone)
class UserPhoneAdmin(admin.ModelAdmin):
    fields = ['user', 'phone', 'primaryuserphone', 'active', 'startdate', 'enddate']
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'created_by'):
            instance.created_by = request.user
        instance.lastmodifyby = request.user
        instance.save()
        form.save_m2m()
        return instance
    list_display = ('user', 'phone', 'primaryuserphone', 'active', 'startdate', 'lastmodifydate')
    ordering = ('user', 'primaryuserphone', 'phone',)
    list_filter = ('active', 'startdate', 'lastmodifydate',)

@admin.register(EmailType)
class EmailTypeAdmin(admin.ModelAdmin):
    fields = ['emailtype', 'active', 'startdate', 'enddate']
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'created_by'):
            instance.created_by = request.user
        instance.lastmodifyby = request.user
        instance.save()
        form.save_m2m()
        return instance
    list_display = ('emailtype', 'active', 'startdate', 'lastmodifydate')
    ordering = ('id',)
    list_filter = ('active', 'startdate', 'lastmodifydate',)

@admin.register(EmailAddress)
class EmailAddressAdmin(admin.ModelAdmin):
    fields = ['emailtype', 'emailaddress', 'active', 'startdate', 'enddate']
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'created_by'):
            instance.created_by = request.user
        instance.lastmodifyby = request.user
        instance.save()
        form.save_m2m()
        return instance
    list_display = ('emailtype', 'emailaddress', 'active', 'startdate', 'lastmodifydate')
    ordering = ('emailtype', 'emailaddress',)
    list_filter = ('active', 'startdate', 'lastmodifydate',)


#admin.site.site_header = 'Proficere Admin Dashboard'
#admin.site.register(SecurityQuestion, SecurityQuestionAdmin)
#admin.site.register(UserProfile, UserProfileAdmin)
#admin.site.register(AddressType, AddressTypeAdmin)
#admin.site.register(Country, CountryAdmin)
#admin.site.register(State, StateAdmin)
#admin.site.register(Address, AddressAdmin)
#admin.site.register(UserAddress, UserAddressAdmin)
#admin.site.register(PhoneType, PhoneTypeAdmin)
#admin.site.register(CountryExchange, CountryExchangeAdmin)
#admin.site.register(Phone, PhoneAdmin)
#admin.site.register(UserPhone, UserPhoneAdmin)
#admin.site.register(EmailType, EmailTypeAdmin)
#admin.site.register(EmailAddress, EmailAddressAdmin)
