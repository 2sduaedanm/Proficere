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
  lastmodifydate = models.DateTimeField(auto_now=True)
#  lastmodifyby = models.ForeignKey(User, related_name="modifier", on_delete=models.CASCADE)

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
  lastmodifydate = models.DateTimeField(auto_now=True)
#  lastmodifyby = models.ForeignKey(User, related_name="modifier", on_delete=models.CASCADE)

class AddressType(models.Model):
  addresstype = models.CharField(max_length=10)
  active = models.BooleanField(default=True)
  startdate = models.DateTimeField(default=datetime.now)
  enddate = models.DateTimeField(default=datetime.strptime(datetime_str,'%m/%d/%Y %H:%M:%S'))
#  enddate = models.DateTimeField(default=d)
  lastmodifydate = models.DateTimeField(auto_now=True)
#  lastmodifyby = models.ForeignKey(User, related_name="modifier", on_delete=models.CASCADE)

  def __str__(self):
      return self.addresstype

class Country(models.Model):
  country = models.CharField(max_length=60)
  active = models.BooleanField(default=True)
  startdate = models.DateTimeField(default=datetime.now)
  enddate = models.DateTimeField(default=datetime.strptime(datetime_str,'%m/%d/%Y %H:%M:%S'))
#  enddate = models.DateTimeField(default=d)
  lastmodifydate = models.DateTimeField(auto_now=True)
#  lastmodifyby = models.ForeignKey(User, related_name="modifier", on_delete=models.CASCADE)

  def __str__(self):
      return self.country

class State(models.Model):
  country = models.ForeignKey(Country, null=True, default=1, on_delete= models.SET_NULL)
  state = models.CharField(max_length=2)
  statename = models.CharField(max_length=60)
  active = models.BooleanField(default=True)
  startdate = models.DateTimeField(default=datetime.now)
  enddate = models.DateTimeField(default=datetime.strptime(datetime_str,'%m/%d/%Y %H:%M:%S'))
#  enddate = models.DateTimeField(default=d)
  lastmodifydate = models.DateTimeField(auto_now=True)
#  lastmodifyby = models.ForeignKey(User, related_name="modifier", on_delete=models.CASCADE)

  def __str__(self):
      return self.state

class Address(models.Model):
  addresstype = models.ForeignKey(AddressType, null=True, on_delete= models.SET_NULL)
  country = models.ForeignKey(Country, null=True, on_delete= models.SET_NULL)
  addressline01 = models.CharField(max_length=60, null=True, blank=True)
  addressline02 = models.CharField(max_length=60, null=True, blank=True)
  addressline03 = models.CharField(max_length=60, null=True, blank=True)
  city = models.CharField(max_length=30, null=True, blank=True)
  state = models.ForeignKey(State, null=True, blank=True, on_delete= models.SET_NULL)
  postalcode = models.CharField(max_length=10, null=True, blank=True)
  active = models.BooleanField(default=True)
  startdate = models.DateTimeField(default=datetime.now)
  enddate = models.DateTimeField(default=datetime.strptime(datetime_str,'%m/%d/%Y %H:%M:%S'))
#  enddate = models.DateTimeField(default=d)
  lastmodifydate = models.DateTimeField(auto_now=True)
#  lastmodifyby = models.ForeignKey(User, related_name="modifier", on_delete=models.CASCADE)

class PhoneType(models.Model):
  phonetype = models.CharField(max_length=10)
  active = models.BooleanField(default=True)
  startdate = models.DateTimeField(default=datetime.now)
  enddate = models.DateTimeField(default=datetime.strptime(datetime_str,'%m/%d/%Y %H:%M:%S'))
#  enddate = models.DateTimeField(default=d)
  lastmodifydate = models.DateTimeField(auto_now=True)
#  lastmodifyby = models.ForeignKey(User, related_name="modifier", on_delete=models.CASCADE)

  def __str__(self):
      return self.phonetype

class CountryExchange(models.Model):
  country = models.ForeignKey(Country, null=True, on_delete= models.SET_NULL)
  countryexchange = models.CharField(max_length=5)
  active = models.BooleanField(default=True)
  startdate = models.DateTimeField(default=datetime.now)
  enddate = models.DateTimeField(default=datetime.strptime(datetime_str,'%m/%d/%Y %H:%M:%S'))
#  enddate = models.DateTimeField(default=d)
  lastmodifydate = models.DateTimeField(auto_now=True)
#  lastmodifyby = models.ForeignKey(User, related_name="modifier", on_delete=models.CASCADE)

  def __str__(self):
      return self.countryexchange

class Phone(models.Model):
  phonetype = models.ForeignKey(PhoneType, null=True, on_delete= models.SET_NULL)
  countryexchange  = models.ForeignKey(CountryExchange, null=True, on_delete= models.SET_NULL)
  phoneno = models.CharField(max_length=10)
  active = models.BooleanField(default=True)
  startdate = models.DateTimeField(default=datetime.now)
  enddate = models.DateTimeField(default=datetime.strptime(datetime_str,'%m/%d/%Y %H:%M:%S'))
#  enddate = models.DateTimeField(default=d)
  lastmodifydate = models.DateTimeField(auto_now=True)
#  lastmodifyby = models.ForeignKey(User, related_name="modifier", on_delete=models.CASCADE)

class EmailType(models.Model):
  emailtype = models.CharField(max_length=10)
  active = models.BooleanField(default=True)
  startdate = models.DateTimeField(default=datetime.now)
  enddate = models.DateTimeField(default=datetime.strptime(datetime_str,'%m/%d/%Y %H:%M:%S'))
#  enddate = models.DateTimeField(default=d)
  lastmodifydate = models.DateTimeField(auto_now=True)
#  lastmodifyby = models.ForeignKey(User, related_name="modifier", on_delete=models.CASCADE)

  def __str__(self):
      return self.emailtype

class EmailAddress(models.Model):
  emailtype = models.ForeignKey(EmailType, null=True, on_delete= models.SET_NULL)
  emailaddress = models.EmailField(max_length=60, null=True, blank=True)
  active = models.BooleanField(default=True)
  startdate = models.DateTimeField(default=datetime.now)
  enddate = models.DateTimeField(default=datetime.strptime(datetime_str,'%m/%d/%Y %H:%M:%S'))
#  enddate = models.DateTimeField(default=d)
  lastmodifydate = models.DateTimeField(auto_now=True)
#  lastmodifyby = models.ForeignKey(User, related_name="modifier", on_delete=models.CASCADE)


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