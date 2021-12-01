from django import forms
from .models import Member 

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['student_name','university_name','phone_number','admission_number','graduation_year','member_image']