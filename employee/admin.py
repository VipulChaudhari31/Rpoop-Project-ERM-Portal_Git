from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(EmployeeDetail)
admin.site.register(EmployeeEducation)
admin.site.register(EmployeeExperience)
admin.site.register(EmployeeLeave)
admin.site.register(EmployeeTask)