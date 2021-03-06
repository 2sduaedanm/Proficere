from django.contrib import admin
from django.contrib.auth.models import Group


# Register your proficere models here.
from .models import *

class ProgressionAdmin(admin.ModelAdmin):
    fields = ['displayorder', 'shortname', 'longname', 'active', 'startdate', 'enddate']
    list_display = ('shortname', 'longname', 'displayorder', 'active', 'lastmodifydate', 'lastmodifyby')
    search_fields = ('shortname', 'longname')
    ordering = ('displayorder',)
    list_filter = ('active', 'startdate',)
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'created_by'):
            instance.created_by = request.user
        instance.lastmodifyby = request.user
        instance.save()
        form.save_m2m()
        return instance

class ChallengeTypeAdmin(admin.ModelAdmin):
    fields = ['displayorder', 'shortname', 'longname', 'active', 'startdate', 'enddate']
    list_display = ('shortname', 'longname', 'displayorder', 'active', 'lastmodifydate', 'lastmodifyby')
    search_fields = ('shortname', 'longname')
    ordering = ('displayorder',)
    list_filter = ('active', 'startdate',)
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'created_by'):
            instance.created_by = request.user
        instance.lastmodifyby = request.user
        instance.save()
        form.save_m2m()
        return instance

class ChallengeAdmin(admin.ModelAdmin):
    fields = ['displayorder', 'shortname', 'longname', 'challengetypeid', 'hints', 'hintsvideo', 'active', 'startdate', 'enddate']
    list_display = ('shortname', 'longname', 'displayorder', 'challengetypeid', 'hints', 'active', 'lastmodifydate', 'lastmodifyby')
    search_fields = ('shortname', 'longname')
    ordering = ('displayorder',)
    list_filter = ('active', 'startdate', 'hintsvideo',)
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'created_by'):
            instance.created_by = request.user
        instance.lastmodifyby = request.user
        instance.save()
        form.save_m2m()
        return instance

class CurriculumAdmin(admin.ModelAdmin):
    fields = ['displayorder', 'shortname', 'longname', 'belt', 'progressionid', 'active', 'startdate', 'enddate']
    list_display = ('shortname', 'longname', 'displayorder', 'active', 'lastmodifydate', 'lastmodifyby')
    search_fields = ('shortname', 'longname', 'belt')
    ordering = ('displayorder',)
    list_filter = ('active', 'startdate',)
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'created_by'):
            instance.created_by = request.user
        instance.lastmodifyby = request.user
        instance.save()
        form.save_m2m()
        return instance

class ChallengeCurriculumAdmin(admin.ModelAdmin):
    fields = ['displayorder', 'curriculumid', 'challengeid', 'active', 'startdate', 'enddate']
    list_display = ('challengeid', 'curriculumid', 'displayorder', 'active', 'lastmodifydate', 'lastmodifyby')
    search_fields = ('curriculumid', 'challengeid')
    ordering = ('displayorder',)
    list_filter = ('active', 'startdate',)
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'created_by'):
            instance.created_by = request.user
        instance.lastmodifyby = request.user
        instance.save()
        form.save_m2m()
        return instance

class StatusAdmin(admin.ModelAdmin):
    fields = ['displayorder', 'shortname', 'active', 'startdate', 'enddate']
    list_display = ('shortname', 'displayorder', 'active', 'lastmodifydate', 'lastmodifyby')
    search_fields = ('shortname', 'active')
    ordering = ('displayorder',)
    list_filter = ('active', 'startdate',)
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'created_by'):
            instance.created_by = request.user
        instance.lastmodifyby = request.user
        instance.save()
        form.save_m2m()
        return instance

class StudentCurriculumAdmin(admin.ModelAdmin):
    fields = ['studentid', 'progressionid', 'curriculumid', 'active', 'statusid', 'startdate', 'enddate']
    list_display = ('studentid', 'progressionid', 'curriculumid', 'active', 'statusid', 'lastmodifydate', 'lastmodifyby')
    search_fields = ('studentid', 'progressionid', 'curriculumid', 'statusid')
    list_filter = ('active', 'startdate',)
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'created_by'):
            instance.created_by = request.user
        instance.lastmodifyby = request.user
        instance.save()
        form.save_m2m()
        return instance

admin.site.register(Progression, ProgressionAdmin)
admin.site.register(ChallengeType, ChallengeTypeAdmin)
admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(Curriculum, CurriculumAdmin)
admin.site.register(ChallengeCurriculum, ChallengeCurriculumAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(StudentCurriculum, StudentCurriculumAdmin)
