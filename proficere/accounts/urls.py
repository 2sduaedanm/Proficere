from django.urls import path

from django.contrib.auth import views as auth_views
from django.contrib import admin

from instruct import views as instruct_views

from . import views



urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('admin/', admin.site.urls),

    path('', views.home, name="home"),
    path('instruct/', instruct_views.instructor_home, name="instructHome"),
    path('student/', instruct_views.student_home, name="studentHome"),
    path('staff/', views.staff_home, name="staffHome"),


#- Submit email form                         //PasswordResetView.as_view()
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
     name="reset_password"),

#- Email sent success message                //PasswordResetDoneView.as_view()
    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
        name="password_reset_done"),

#- Link to password Reset form in email       //PasswordResetConfirmView.as_view()
    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
     name="password_reset_confirm"),

#- Password successfully changed message     //PasswordResetCompleteView.as_view()
    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), 
        name="password_reset_complete"),


]