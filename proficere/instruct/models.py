from django.contrib.auth import get_user_model
from django.db import models
#from django.db.models import Q
#from django.db.models.constraints import UniqueConstraint
from datetime import datetime

User = get_user_model()

#d = datetime(2999, 12, 31, 23, 55, 59, 342380)
datetime_str = '12/31/2999 23:59:59'

# Create proficere Models here.

class Progression(models.Model):
    shortname = models.CharField(max_length=60)
    longname = models.CharField(max_length=255)
    displayorder = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)
    startdate = models.DateTimeField(default=datetime.now)
    enddate = models.DateTimeField(default=datetime.strptime(datetime_str,'%m/%d/%Y %H:%M:%S'))
    lastmodifydate = models.DateTimeField(auto_now=True)
    lastmodifyby = models.ForeignKey(User, related_name='%(class)s_modifier', null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.shortname

class Curriculum (models.Model):
    shortname = models.CharField(max_length=60)
    longname = models.CharField(max_length=255)
    belt = models.CharField(max_length=100, blank=True) #image
    progressionid = models.ForeignKey(Progression, default=1, on_delete=models.CASCADE)
    displayorder = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)
    startdate = models.DateTimeField(default=datetime.now)
    enddate = models.DateTimeField(default=datetime.strptime(datetime_str,'%m/%d/%Y %H:%M:%S'))
    lastmodifydate = models.DateTimeField(auto_now=True)
    lastmodifyby = models.ForeignKey(User, related_name='%(class)s_modifier', null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.shortname

class ChallengeType(models.Model):
    shortname = models.CharField(max_length=60)
    longname = models.CharField(max_length=255)
    displayorder = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)
    startdate = models.DateTimeField(default=datetime.now)
    enddate = models.DateTimeField(default=datetime.strptime(datetime_str,'%m/%d/%Y %H:%M:%S'))
    lastmodifydate = models.DateTimeField(auto_now=True)
    lastmodifyby = models.ForeignKey(User, related_name='%(class)s_modifier', null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.shortname

class Challenge (models.Model):
    shortname = models.CharField(max_length=60)
    longname = models.CharField(max_length=255)
    challengetypeid = models.ForeignKey(ChallengeType, on_delete=models.CASCADE)
    displayorder = models.IntegerField(blank=True, null=True)
    hints = models.CharField(max_length=255, blank=True)
    hintsvideo = models.FileField(upload_to='hintsVideos/')
    active = models.BooleanField(default=True)
    startdate = models.DateTimeField(default=datetime.now)
    enddate = models.DateTimeField(default=datetime.strptime(datetime_str,'%m/%d/%Y %H:%M:%S'))
    lastmodifydate = models.DateTimeField(auto_now=True)
    lastmodifyby = models.ForeignKey(User, related_name='%(class)s_modifier', null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.shortname


class ChallengeCurriculum (models.Model):
    challengeid = models.ForeignKey(Challenge, related_name='challengecurriculums',on_delete=models.CASCADE)
    curriculumid = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
#    progressionid = models.ForeignKey(Progression, default=1, on_delete=models.CASCADE)
    displayorder = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)
    startdate = models.DateTimeField(default=datetime.now)
    enddate = models.DateTimeField(default=datetime.strptime(datetime_str,'%m/%d/%Y %H:%M:%S'))
    lastmodifydate = models.DateTimeField(auto_now=True)
    lastmodifyby = models.ForeignKey(User, related_name='%(class)s_modifier', null=True, on_delete=models.DO_NOTHING)

#class StudentProgression (models.Model):
#    studentid = models.ForeignKey(User, on_delete=models.CASCADE)
#    progressionid = models.ForeignKey(Progression, default=1, on_delete=models.CASCADE)
#    active = models.BooleanField(default=True)
#    startdate = models.DateTimeField(default=datetime.now)
#    enddate = models.DateTimeField(default=datetime.strptime(datetime_str,'%m/%d/%Y %H:%M:%S'))
#    lastmodifydate = models.DateTimeField(auto_now=True)
#    lastmodifyby = models.ForeignKey(User, related_name='%(class)s_modifier', on_delete=models.DO_NOTHING)


class Status (models.Model):
    shortname = models.CharField(max_length=60)
#    longname = models.CharField(max_length=255)
    displayorder = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)
    startdate = models.DateTimeField(default=datetime.now)
    enddate = models.DateTimeField(default=datetime.strptime(datetime_str,'%m/%d/%Y %H:%M:%S'))
    lastmodifydate = models.DateTimeField(auto_now=True)
    lastmodifyby = models.ForeignKey(User, related_name='%(class)s_modifier', null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.shortname
      
class StudentCurriculum (models.Model):
    studentid = models.ForeignKey(User, on_delete=models.CASCADE)
    curriculumid = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    progressionid = models.ForeignKey(Progression, default=1, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    statusid = models.ForeignKey(Status, on_delete=models.CASCADE)
    startdate = models.DateTimeField(default=datetime.now)
    enddate = models.DateTimeField(default=datetime.strptime(datetime_str,'%m/%d/%Y %H:%M:%S'))
    lastmodifydate = models.DateTimeField(auto_now=True)
    lastmodifyby = models.ForeignKey(User, related_name='%(class)s_modifier', null=True, on_delete=models.DO_NOTHING)

class StudentChallengeEvent (models.Model):
    progressionid = models.ForeignKey(Progression, default=1, on_delete=models.CASCADE)
    studentid = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student_user")
    curriculumid = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    challengeid = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    assessdate = models.DateTimeField(default=datetime.now)
    instructorid = models.ForeignKey(User, on_delete=models.CASCADE, related_name="instructor_user")
    resultcode = models.BooleanField(default=False)
    videofile = models.CharField(blank=True,max_length=255)
