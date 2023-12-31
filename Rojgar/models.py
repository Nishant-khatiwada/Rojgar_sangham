from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django import forms
# Create your models here.

class user_request(models.Model):
    name=models.CharField( max_length=50)
    phone=models.IntegerField((""))
    address=models.CharField( max_length=50)
    district = models.CharField(max_length=50 ,default ="")
    email=models.CharField( max_length=50)
    work_done = models.BooleanField(default = False)
    SELECTED_AREA = [
    ('EL', 'Electrical Services'),
    ('CA', 'Carpentry'),
    ('AR', 'Appliance Repair'),
    ('PA', 'Painting'),
    ('GA', 'Gardening/Landscaping'),
    ('RO', 'Roofing'),
    ('HV', 'HVAC (Heating, Ventilation, and Air Conditioning)'),
    ('FI', 'Flooring Installation/Repair'),
    ('WI', 'Window Installation/Repair'),
    ('LO', 'Locksmith Services'),
    ('PC', 'Pest Control'),
    ('DI', 'Drywall Installation/Repair'),
    ('FA', 'Furniture Assembly'),
    ('PW', 'Pressure Washing'),
    ('TI', 'Tile Installation/Repair'),
    ('HS', 'Home Security Installation'),
    ('ST', 'Septic Tank Maintenance'),
    ('GD', 'Garage Door Installation/Repair'),
    ('CS', 'Chimney Sweeping/Repair'),
    ('CI', 'Cabinet Installation/Repair'),
    ('FI', 'Fence Installation/Repair'),
    ('DC', 'Deck Construction/Repair'),
    ('GU', 'Gutter Cleaning/Installation'),
    ('CW', 'Concrete Work'),
    ('HT', 'Home Theater Installation'),
    ('PL', 'Plastering'),
    ('WP', 'Waterproofing'),
    ('SI', 'Solar Panel Installation'),
    ('ID', 'Interior Design'),
    ('HI', 'Home Inspection Services'),
    ('OT', 'Others'),
    ]
    selected=models.CharField(max_length=30, choices=SELECTED_AREA,default="")
    problem=models.TextField()
    date=models.DateField()
    accepted_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='accepted_requests')
    is_accepted = models.BooleanField(default=False)
    accepted_date=models.DateField(null=True)

    def __str__(self):
        return(self.email)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_token = models.CharField(max_length=125,default="")
    is_verified = models.BooleanField(default="")
class UserData(models.Model):
    user_name = models.CharField(max_length=30,default="",unique=True)
    first_name = models.CharField(max_length=20,default="")
    last_name = models.CharField(max_length=20,default="")
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    # Add a field for the radio button
    gender = forms.ChoiceField(
        choices=GENDER,
        widget=forms.RadioSelect,
        required=True,
    )
    email = models.EmailField(default="",primary_key=True)
    phone = models.CharField(max_length=14)
    def __str__(self):
        return(self.email)
class WorkerStat(models.Model): 
    email = models.CharField(max_length=50)
    WORK_AREAS = [
    ('EL', 'Electrical Services'),
    ('CA', 'Carpentry'),
    ('AR', 'Appliance Repair'),
    ('PA', 'Painting'),
    ('GA', 'Gardening/Landscaping'),
    ('RO', 'Roofing'),
    ('HV', 'HVAC (Heating, Ventilation, and Air Conditioning)'),
    ('FI', 'Flooring Installation/Repair'),
    ('WI', 'Window Installation/Repair'),
    ('LO', 'Locksmith Services'),
    ('PC', 'Pest Control'),
    ('DI', 'Drywall Installation/Repair'),
    ('FA', 'Furniture Assembly'),
    ('PW', 'Pressure Washing'),
    ('TI', 'Tile Installation/Repair'),
    ('HS', 'Home Security Installation'),
    ('ST', 'Septic Tank Maintenance'),
    ('GD', 'Garage Door Installation/Repair'),
    ('CS', 'Chimney Sweeping/Repair'),
    ('CI', 'Cabinet Installation/Repair'),
    ('FI', 'Fence Installation/Repair'),
    ('DC', 'Deck Construction/Repair'),
    ('GU', 'Gutter Cleaning/Installation'),
    ('CW', 'Concrete Work'),
    ('HT', 'Home Theater Installation'),
    ('PL', 'Plastering'),
    ('WP', 'Waterproofing'),
    ('SI', 'Solar Panel Installation'),
    ('ID', 'Interior Design'),
    ('HI', 'Home Inspection Services'),
    ('OT', 'Others'),
    ]
    
    workarea = models.CharField(max_length=30, choices=WORK_AREAS,default="")
    father_name = models.CharField(max_length=30, default="")
    grand_father_name = models.CharField(max_length=30, default="")
    temporary_address = models.CharField(max_length=30, default="")
    permanent_address = models.CharField(max_length=30, default="")
    citizenship_image_front = models.ImageField(upload_to="media/",default="")
    citizenship_image_back = models.ImageField(upload_to="media/",default="")
    worker_district =models.CharField(max_length=50,default="")


class ContactForm(models.Model):
    name = models.CharField(default="",max_length=50)
    email = models.CharField(default="",max_length=50)
    subject = models.CharField(default="",max_length=50)
    message = models.TextField(default="")


    def __str__(self):
        return self.email
    worker_district =models.CharField(max_length=50,default="")