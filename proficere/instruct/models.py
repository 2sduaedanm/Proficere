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
    displayorder = models.IntegerField()
    active = models.BooleanField(default=True)
    startdate = models.DateTimeField(default=datetime.now)
    enddate = models.DateTimeField(default=datetime.strptime(datetime_str,'%m/%d/%Y %H:%M:%S'))
#    enddate = models.DateTimeField(default=d)
    lastmodifyby = models.ForeignKey(
      get_user_model(),
      null=True,
      on_delete=models.CASCADE
    )
#    lastmodifydatetime = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.shortname

class Curriculum (models.Model):
    shortname = models.CharField(max_length=60)
    longname = models.CharField(max_length=255)
    belt = models.CharField(max_length=100, blank=True) #image
    progressionid = models.ForeignKey(Progression, default=1, on_delete=models.CASCADE)
    displayorder = models.IntegerField()
    active = models.BooleanField(default=True)
    startdate = models.DateTimeField(default=datetime.now)
    enddate = models.DateTimeField(default=datetime.strptime(datetime_str,'%m/%d/%Y %H:%M:%S'))
    lastmodifyby = models.ForeignKey(
      get_user_model(),
      null=True,
      on_delete=models.CASCADE
    )

    def __str__(self):
        return self.shortname

class ChallengeType(models.Model):
    shortname = models.CharField(max_length=60)
    longname = models.CharField(max_length=255)
    displayorder = models.IntegerField()
    active = models.BooleanField(default=True)
    startdate = models.DateTimeField(default=datetime.now)
    enddate = models.DateTimeField(default=datetime.strptime(datetime_str,'%m/%d/%Y %H:%M:%S'))
    lastmodifyby = models.ForeignKey(
      get_user_model(),
      null=True,
      on_delete=models.CASCADE
    )

    def __str__(self):
        return self.shortname

class Challenge (models.Model):
    shortname = models.CharField(max_length=60)
    longname = models.CharField(max_length=255)
    challengetypeid = models.ForeignKey(ChallengeType, on_delete=models.CASCADE)
    displayorder = models.IntegerField()
    hints = models.CharField(max_length=255, blank=True)
    hintsvideo = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(default=True)
    startdate = models.DateTimeField(default=datetime.now)
    enddate = models.DateTimeField(default=datetime.strptime(datetime_str,'%m/%d/%Y %H:%M:%S'))
    lastmodifyby = models.ForeignKey(
      get_user_model(),
      null=True,
      on_delete=models.CASCADE
    )

    def __str__(self):
        return self.shortname


class ChallengeCurriculum (models.Model):
    challengeid = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    curriculumid = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
#    progressionid = models.ForeignKey(Progression, default=1, on_delete=models.CASCADE)
    displayorder = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)
    startdate = models.DateTimeField(default=datetime.now)
    enddate = models.DateTimeField(default=datetime.strptime(datetime_str,'%m/%d/%Y %H:%M:%S'))
    lastmodifyby = models.ForeignKey(
      get_user_model(),
      null=True,
      on_delete=models.CASCADE
    )

#class StudentProgression (models.Model):
#    studentid = models.ForeignKey(User, on_delete=models.CASCADE)
#    progressionid = models.ForeignKey(Progression, default=1, on_delete=models.CASCADE)
#    active = models.BooleanField(default=True)
#    startdate = models.DateTimeField(default=datetime.now)
#    enddate = models.DateTimeField(default=datetime.strptime(datetime_str,'%m/%d/%Y %H:%M:%S'))
#    lastmodifyby = models.ForeignKey(
#      get_user_model(),
#      null=True,
#      on_delete=models.CASCADE
#    )

class StudentCurriculum (models.Model):
    studentid = models.ForeignKey(User, on_delete=models.CASCADE)
    curriculumid = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    progressionid = models.ForeignKey(Progression, default=1, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    startdate = models.DateTimeField(default=datetime.now)
    enddate = models.DateTimeField(default=datetime.strptime(datetime_str,'%m/%d/%Y %H:%M:%S'))
    lastmodifyby = models.ForeignKey(
      get_user_model(),
      related_name='%(class)s_requests_created', 
      null=True,
      on_delete=models.CASCADE
    )

