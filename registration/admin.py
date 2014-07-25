from django.contrib import admin

from registration.models import Student, StaffMember, FacultyMember
from registration.models import TeachingAssistant, Department, Location, Course
from registration.models import TimeSlot, Section


# Register your models here.


admin.site.register(Student)
admin.site.register(StaffMember)
admin.site.register(FacultyMember)
admin.site.register(TeachingAssistant)
admin.site.register(Department)
admin.site.register(Location)
admin.site.register(Course)
admin.site.register(TimeSlot)
admin.site.register(Section)

