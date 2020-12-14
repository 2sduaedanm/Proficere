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

class AnswerTypeAdmin(admin.ModelAdmin):
    fields = ['displayorder', 'shortname', 'longname', 'active', 'startdate','enddate', 'lastmodifyby']
    list_display = ('shortname', 'longname','displayorder', 'active', 'startdate', 'lastmodifyby')
    search_fields = ('shortname','longname')
    ordering = ('displayorder',)
    list_filter = ('active', 'startdate',)

class ChallengeAdmin(admin.ModelAdmin):
    fields = ['displayorder', 'shortname', 'longname', 'challengetypeid', 'answertypeid', 'hints', 'hintsvideo', 'active', 'startdate','enddate', 'lastmodifyby']
    list_display = ('shortname', 'longname','displayorder', 'challengetypeid', 'answertypeid', 'hints', 'active', 'startdate', 'lastmodifyby')
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
    fields = ['displayorder', 'progressionid', 'curriculumid', 'challengeid', 'active', 'startdate','enddate', 'lastmodifyby']
    list_display = ('challengeid', 'curriculumid', 'progressionid', 'displayorder', 'active', 'startdate', 'lastmodifyby')
    search_fields = ('progressionid','curriculumid', 'challengeid')
    ordering = ('displayorder',)
    list_filter = ('active', 'startdate',)


admin.site.register(Progression, ProgressionAdmin)
admin.site.register(AnswerType, AnswerTypeAdmin)
admin.site.register(ChallengeType, ChallengeTypeAdmin)
admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(Curriculum, CurriculumAdmin)
admin.site.register(ChallengeCurriculum, ChallengeCurriculumAdmin)
