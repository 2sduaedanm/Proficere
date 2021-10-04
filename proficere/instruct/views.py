from django.shortcuts import render, redirect 
from django.urls import reverse
from urllib.parse import urlencode
from django.http import HttpResponse
#from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .models import *
from .forms import CreateUserForm
from django.db.models import Q

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# Create your views here.

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'instruct/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'instruct/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def home(request):
	context = {}

	return render(request, 'instruct/dashboard.html', context)


@login_required(login_url='login')
def instructor_home(request):
	context = {}

	return render(request, 'instruct/dashboard.html', context)


@login_required(login_url='login')
def student_home(request):
	#We should find some way to order after we find the objects.filter
	pastProgressions = StudentCurriculum.objects.filter(studentid= request.user, statusid = 3)
	currentProgressions = StudentCurriculum.objects.filter(studentid= request.user, statusid__in = [1,2])
	context = {"pastProgressions":pastProgressions,"currentProgressions":currentProgressions}

	return render(request, 'instruct/studentHome.html', context)

@login_required(login_url='login')
def display_curriculum_challenges(request,curriculumid):
	challengeList = ChallengeCurriculum.objects.filter(curriculumid= curriculumid)
	curriculum = Curriculum.objects.get(id=curriculumid)
	context = {"curriculum":curriculum, "challengeList":challengeList}

	return render(request, 'instruct/CurriculumOverview.html', context)

@login_required(login_url='login')
def display_progression_curriculums(request,progressionid):
	curriculumList = Curriculum.objects.filter(progressionid= progressionid)
	context = {"curriculumList":curriculumList}

	return render(request, 'instruct/ProgressionOverview.html', context)

@login_required(login_url='login')
def instructStudentChallenge_select(request):
	context = {}
	curriculumid = request.GET.get('curriculum')
	studentid = request.GET.get('student')
	searched = request.POST.get('searched')

	#If no curriculumid is present, get and show the list of curriculum for that student
	if(studentid):
		student = User.objects.get(id=studentid)
		if searched:
			currentCurriculumList = Curriculum.objects.filter(studentcurriculum__in=StudentCurriculum.objects.filter(studentid= student.id, statusid__in = [1,2])).filter(Q(longname__contains = searched)).order_by('progressionid')
			if (not curriculumid) & (not currentCurriculumList):
				currentCurriculumList = Curriculum.objects.filter(studentcurriculum__in=StudentCurriculum.objects.filter(studentid= student.id, statusid__in = [1,2])).order_by('progressionid')
				context.update({"search_error":searched})
		else:
			currentCurriculumList = Curriculum.objects.filter(studentcurriculum__in=StudentCurriculum.objects.filter(studentid= student.id, statusid__in = [1,2])).order_by('progressionid')
		context.update({"student":student,"curriculumList":currentCurriculumList})
	if(curriculumid):
		curriculum = Curriculum.objects.get(id=curriculumid)
		if searched:
			challengeList = Challenge.objects.filter(challengecurriculums__curriculumid=curriculum.id).filter(longname__contains = searched)
			if (not challengeList):
				challengeList = Challenge.objects.filter(challengecurriculums__curriculumid=curriculum.id)
				context.update({"search_error":searched})
		else:
			challengeList = Challenge.objects.filter(challengecurriculums__curriculumid=curriculum.id)
		sce_list = StudentChallengeEvent.objects.filter(studentid=studentid, curriculumid=curriculumid, progressionid=curriculum.progressionid).order_by('challengeid','-assessdate').distinct('challengeid')
		context.update({"curriculum":curriculum, "challengeList":challengeList,"sce_list":sce_list})
		

	#If no studentid is present, get and show the list of students
	if searched:
		studentList = User.objects.filter(groups__name = 'Student').filter(Q(username__contains = searched)|Q(last_name__contains = searched)|Q(first_name__contains = searched)).order_by('last_name','first_name')
		if (not studentid) & (not curriculumid) & (not studentList):
				studentList = User.objects.filter(groups__name = 'Student').order_by('last_name','first_name')
				context.update({"search_error":searched})
	else:
		studentList = User.objects.filter(groups__name = 'Student').order_by('last_name','first_name')
	context.update({"studentList":studentList})

	return render(request, 'instruct/InstructStudentSelect.html', context)

@login_required(login_url='login')
def instructStudentChallenge(request):

	challengeid = request.GET.get('challenge')
	curriculumid = request.GET.get('curriculum')
	studentid = request.GET.get('student')

	challenge = Challenge.objects.get(id=challengeid)
	curriculum = Curriculum.objects.get(id=curriculumid)
	student = User.objects.get(id=studentid)
	sce_list = StudentChallengeEvent.objects.filter(studentid=studentid, curriculumid=curriculumid, progressionid=curriculum.progressionid)
	context = {"student":student, "curriculum":curriculum, "challenge":challenge, "sce_list":sce_list}

	return render(request, 'instruct/InstructStudentChallenge.html', context)

@login_required(login_url='login')
def instructStudentChallenge_Submit(request):
	challengeid = request.POST.get('challenge')
	curriculumid = request.POST.get('curriculum')
	progressionid = request.POST.get('progression')
	studentid = request.POST.get('student')

	#Save the event
	progression = Progression.objects.get(id=progressionid)
	student = User.objects.get(id=studentid)
	curriculum = Curriculum.objects.get(id=curriculumid)
	challenge = Challenge.objects.get(id=challengeid)
	if(request.POST.get('resultCode') == "pass"):
		StudentChallengeEvent.objects.create(progressionid=progression,studentid=student,curriculumid=curriculum,challengeid=challenge,instructorid=request.user,resultcode=True)
	else:
		StudentChallengeEvent.objects.create(progressionid=progression,studentid=student,curriculumid=curriculum,challengeid=challenge,instructorid=request.user,resultcode=False)

	#Save the recoding
	#if 'recodingBlob' in request.POST:
	recording = request.FILES.get('recordingBlob')
	path = default_storage.save('ChallengeRecordings/'+recording.name, ContentFile(recording.read()))


	#Reroute back to ChallengeSelection for that same Student + Curriculum
	base_url = reverse('instructStudentChallenge_select')  # 1 /products/
	query_string =  urlencode({'student': studentid,'curriculum':curriculumid})  # 2 category=42
	url = '{}?{}'.format(base_url, query_string)  # 3 /products/?category=42

	return redirect(url)