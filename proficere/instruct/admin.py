from django.contrib import admin
from django.contrib.auth.models import User, Group


# Register your proficere models here.
from .models import *


@admin.register(Progression)
class ProgressionAdmin(admin.ModelAdmin):
    fields = ['displayorder', 'shortname',
              'longname', 'active', 'startdate', 'enddate']
    list_display = ('shortname', 'longname', 'displayorder',
                    'active', 'lastmodifydate', 'lastmodifyby')
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


@admin.register(ChallengeType)
class ChallengeTypeAdmin(admin.ModelAdmin):
    fields = ['displayorder', 'shortname',
              'longname', 'active', 'startdate', 'enddate']
    list_display = ('shortname', 'longname', 'displayorder',
                    'active', 'lastmodifydate', 'lastmodifyby')
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


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    fields = ['displayorder', 'shortname', 'longname', 'challengetypeid',
              'hints', 'hintsvideo', 'active', 'startdate', 'enddate']
    list_display = ('shortname', 'longname', 'displayorder', 'challengetypeid',
                    'hints', 'hintsvideo', 'active', 'lastmodifydate', 'lastmodifyby')
    search_fields = ['shortname', 'longname', 'challengetypeid__shortname']
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


@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    fields = ['displayorder', 'shortname', 'longname', 'belt',
              'progressionid', 'active', 'startdate', 'enddate']
    list_display = ('shortname', 'longname', 'displayorder',
                    'active', 'lastmodifydate', 'lastmodifyby')
    search_fields = ['shortname', 'longname', 'belt',
                     'progressionid__shortname']
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


@admin.register(ChallengeCurriculum)
class ChallengeCurriculumAdmin(admin.ModelAdmin):
    fields = ['displayorder', 'curriculumid',
              'challengeid', 'active', 'startdate', 'enddate']
    list_display = ('challengeid', 'curriculumid', 'displayorder',
                    'active', 'lastmodifydate', 'lastmodifyby')
    search_fields = ['curriculumid__shortname', 'curriculumid__longname',
                     'challengeid__shortname', 'challengeid__longname']
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


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    fields = ['displayorder', 'shortname', 'active', 'startdate', 'enddate']
    list_display = ('shortname', 'displayorder', 'active',
                    'lastmodifydate', 'lastmodifyby')
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


@admin.register(StudentCurriculum)
class StudentCurriculumAdmin(admin.ModelAdmin):
    fields = ['studentid', 'progressionid', 'curriculumid',
              'active', 'statusid', 'startdate', 'enddate']
    list_display = ('studentid', 'progressionid', 'curriculumid',
                    'active', 'statusid', 'lastmodifydate', 'lastmodifyby')
    search_fields = ['studentid__username',
                     'progressionid__shortname',
                     'curriculumid__shortname', 'curriculumid__longname']
    list_filter = ('active', 'startdate',)

    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'created_by'):
            instance.created_by = request.user
        instance.lastmodifyby = request.user
        instance.save()
        form.save_m2m()
        return instance


@admin.register(StudentChallengeEvent)
class StudentChallengeEventAdmin(admin.ModelAdmin):
    fields = ['progressionid', 'studentid', 'curriculumid', 'challengeid',
              'instructorid', 'assessdate', 'resultcode', 'videofile', 'comment']
    list_display = ('progressionid', 'studentid', 'curriculumid', 'challengeid',
                    'instructorid', 'assessdate', 'resultcode', 'videofile', 'comment')
    search_fields = ['studentid__username',
                     'progressionid__shortname',
                     'curriculumid__shortname', 'curriculumid__longname',
                     'challengeid__shortname', 'challengeid__longname']
    ordering = ('assessdate',)
    list_filter = ('resultcode', 'assessdate',)

    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'created_by'):
            instance.created_by = request.user
        instance.lastmodifyby = request.user
        instance.save()
        form.save_m2m()
        return instance


#admin.site.register(Progression, ProgressionAdmin)
#admin.site.register(ChallengeType, ChallengeTypeAdmin)
#admin.site.register(Challenge, ChallengeAdmin)
#admin.site.register(Curriculum, CurriculumAdmin)
#admin.site.register(ChallengeCurriculum, ChallengeCurriculumAdmin)
#admin.site.register(Status, StatusAdmin)
#admin.site.register(StudentCurriculum, StudentCurriculumAdmin)
#admin.site.register(StudentChallengeEvent, StudentChallengeEventAdmin)
