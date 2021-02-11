from django.urls import path

from django.contrib.auth import views as auth_views
from django.contrib import admin

from . import views



urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name="home"),
    #ex: /instruct/curriculum/1
    path('curriculum/<int:curriculumid>', views.display_curriculum_challenges, name="display_curriculum_challenges"),
    path('progression/<int:progressionid>', views.display_progression_curriculums, name="display_progression_curriculums"),
    
]