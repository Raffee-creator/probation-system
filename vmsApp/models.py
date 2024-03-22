from email.policy import default
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
import qrcode
from PIL import Image
from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager



# Create your models here.
class Departments(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    status = models.CharField(max_length=2, choices=(('1','Active'), ('2','Inactive')), default = 1)
    delete_flag = models.IntegerField(default = 0)
    date_added = models.DateTimeField(default = timezone.now)
    date_created = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = "List of Departments"

    def __str__(self):
        return str(f"{self.name}")

class Visitors(models.Model):
    department = models.ForeignKey(Departments, on_delete = models.CASCADE, related_name='department')
    court_id = models.CharField(max_length=250)
    case_id = models.CharField(max_length=200, default='No case ID')
    person_id = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    gender = models.CharField(max_length=20, choices=(('Male','Male'), ('Female','Female')), default = 'Male')
    contact = models.CharField(max_length=250, null=True, blank = True)
    email = models.CharField(max_length=250, null=True, blank = True)
    address = models.TextField()
    reason = models.TextField()
    comment = models.TextField(max_length=200, default='No comment')
    date_added = models.DateTimeField(default = timezone.now)


    class Meta:
        verbose_name_plural = "List of Offender Logs"

    def __str__(self):
        return str(f"{self.name}")

