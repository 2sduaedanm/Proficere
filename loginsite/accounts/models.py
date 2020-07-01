from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime

User = get_user_model()

#d = datetime(2999, 12, 31, 23, 55, 59, 342380)
datetime_str = '12/31/2999 23:59:59'

# Create your models here.

class SecurityQuestion(models.Model):
  securityquestion = models.CharField(max_length=60)
  active = models.BooleanField(default=True)
  startdate = models.DateTimeField(default=datetime.now)
  enddate = models.DateTimeField(default=datetime.strptime(datetime_str,'%m/%d/%Y %H:%M:%S'))
#  enddate = models.DateTimeField(default=d)
  lastmodifyby = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
  lastmodifydate = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.securityquestion

class UserProfile(models.Model):
  user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
  birthdate = models.DateField()
#  userphoto = models.ImageField(default='profile1.png', null=True, blank=True)
  active = models.BooleanField(default=True)
  startdate = models.DateTimeField(default=datetime.now)
  enddate = models.DateTimeField(default=datetime.strptime(datetime_str,'%m/%d/%Y %H:%M:%S'))
#  enddate = models.DateTimeField(default=d)
  lastmodifyby = models.ForeignKey(User, related_name="modifier", on_delete=models.CASCADE)
  lastmodifydate = models.DateTimeField(auto_now=True)

#class Customer(models.Model):
#	name = models.CharField(max_length=200, null=True)
#	phone = models.CharField(max_length=200, null=True)
#	email = models.CharField(max_length=200, null=True)
#	date_created = models.DateTimeField(auto_now_add=True, null=True)

#	def __str__(self):
#		return self.name


#class Tag(models.Model):
#	name = models.CharField(max_length=200, null=True)

#	def __str__(self):
#		return self.name

#class Product(models.Model):
#	CATEGORY = (
#			('Indoor', 'Indoor'),
#			('Out Door', 'Out Door'),
#			) 

#	name = models.CharField(max_length=200, null=True)
#	price = models.FloatField(null=True)
#	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
#	description = models.CharField(max_length=200, null=True, blank=True)
#	date_created = models.DateTimeField(auto_now_add=True, null=True)
#	tags = models.ManyToManyField(Tag)

#	def __str__(self):
#		return self.name

#class Order(models.Model):
#	STATUS = (
#			('Pending', 'Pending'),
#			('Out for delivery', 'Out for delivery'),
#			('Delivered', 'Delivered'),
#			)

#	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
#	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
#	date_created = models.DateTimeField(auto_now_add=True, null=True)
#	status = models.CharField(max_length=200, null=True, choices=STATUS)
#	note = models.CharField(max_length=1000, null=True)

#	def __str__(self):
#		return self.product.name