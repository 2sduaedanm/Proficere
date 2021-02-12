from django.contrib import admin
from django.contrib.auth.models import Group


# Register your proficere models here.
from .models import *

class ProgressionAdmin(admin.ModelAdmin):
    fields = ['displayorder', 'shortname', 'longname', 'active', 'startdate','enddate', 'lastmodifyby']
    list_display = ('shortname', 'longname','displayorder', 'active', 'startdate', 'lastmodifyby')
    search_fields = ('shortname','longname')
    ordering = ('displayorder',)
    list_filter = ('active', 'startdate',)

class ChallengeTypeAdmin(admin.ModelAdmin):
    fields = ['displayorder', 'shortname', 'longname', 'active', 'startdate','enddate', 'lastmodifyby']
    list_display = ('shortname', 'longname','displayorder', 'active', 'startdate', 'lastmodifyby')
    search_fields = ('shortname','longname')
    ordering = ('displayorder',)
    list_filter = ('active', 'startdate',)

class ChallengeAdmin(admin.ModelAdmin):
    fields = ['displayorder', 'shortname', 'longname', 'challengetypeid', 'hints', 'hintsvideo', 'active', 'startdate','enddate', 'lastmodifyby']
    list_display = ('shortname', 'longname','displayorder', 'challengetypeid', 'hints', 'active', 'startdate', 'lastmodifyby')
    search_fields = ('shortname','longname')
    ordering = ('displayorder',)
    list_filter = ('active', 'startdate', 'hintsvideo',)

class CurriculumAdmin(admin.ModelAdmin):
    fields = ['displayorder', 'shortname', 'longname', 'belt', 'progressionid', 'active', 'startdate','enddate', 'lastmodifyby']
    list_display = ('shortname', 'longname','displayorder', 'active', 'startdate', 'lastmodifyby')
    search_fields = ('shortname','longname', 'belt')
    ordering = ('displayorder',)
    list_filter = ('active', 'startdate',)

class ChallengeCurriculumAdmin(admin.ModelAdmin):
    fields = ['displayorder', 'curriculumid', 'challengeid', 'active', 'startdate','enddate', 'lastmodifyby']
    list_display = ('challengeid', 'curriculumid', 'displayorder', 'active', 'startdate', 'lastmodifyby')
    search_fields = ('curriculumid', 'challengeid')
    ordering = ('displayorder',)
    list_filter = ('active', 'startdate',)

class StudentCurriculumAdmin(admin.ModelAdmin):
    fields = ['studentid', 'progressionid', 'curriculumid', 'active', 'startdate','enddate', 'lastmodifyby']
    list_display = ('studentid', 'progressionid', 'curriculumid', 'active', 'startdate', 'lastmodifyby')
    search_fields = ('studentid', 'progressionid', 'curriculumid')
    list_filter = ('active', 'startdate',)


admin.site.register(Progression, ProgressionAdmin)
admin.site.register(ChallengeType, ChallengeTypeAdmin)
admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(Curriculum, CurriculumAdmin)
admin.site.register(ChallengeCurriculum, ChallengeCurriculumAdmin)
admin.site.register(StudentCurriculum, StudentCurriculumAdmin)
