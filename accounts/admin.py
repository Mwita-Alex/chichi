from django.contrib import admin
from .models import Member

# Register your models here.
@admin.register(Member)
class MembersAdmin(admin.ModelAdmin):
    list_display=['student_name','university_name','phone_number','admission_number']

