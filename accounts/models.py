from django.db import models
from django.contrib.auth.models import User

#registration model .
class Member(models.Model):
    student_name = models.CharField(max_length=200)
    university_name = models.CharField(max_length = 255)
    phone_number = models.CharField(max_length = 13)
    admission_number = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete =models.CASCADE,null=True)
    graduation_year = models.CharField(max_length=200,null=True)
    member_image = models.ImageField(upload_to='accounts/images/', null=True, blank=True)


