from django.urls import path

from django.contrib.auth import views as auth_views
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # ex: /instruct/curriculum/1
    path('curriculum/<int:curriculumid>', views.display_curriculum_challenges,
         name="display_curriculum_challenges"),
    path('progression/<int:progressionid>', views.display_progression_curriculums,
         name="display_progression_curriculums"),
    path('instructStudentChallengeSelect', views.instructStudentChallenge_select,
         name="instructStudentChallenge_select"),
    path('InstructStudentChallenge', views.instructStudentChallenge,
         name="instructStudentChallenge"),
    path('InstructStudentChallenge_Submit', views.instructStudentChallenge_Submit,
         name="instructStudentChallenge_Submit"),
    path('instruct/signUpClass', views.signUpClassView, name="signUpClass"),
    path('instruct/signupClassStudent_select',
         views.signupClassStudentView, name="signUpClassStudent"),


]
