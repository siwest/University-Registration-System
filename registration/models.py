from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class StaffMember(models.Model):
    ssn = models.CharField(max_length=9)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    salary = models.IntegerField(default=0)

    def __unicode__(self):
        return self.first_name + " " + self.last_name + " (" + self.ssn + ")"


class FacultyMember(models.Model):
    staff = models.ForeignKey(StaffMember)
    rank = models.CharField(max_length=50, default="Jr.")
    course_load = models.IntegerField(default=1)

    def __unicode__(self):
        return self.staff.first_name + " " + self.staff.last_name + " (" + self.staff.ssn + ")"




class Location(models.Model):
    building = models.CharField(max_length=20)
    room = models.CharField(max_length=5)
    equipment = models.CharField(max_length=100)
    capacity = models.IntegerField(default=0)

    def __unicode__(self):
        return "Building " + self.building + ", Room " + self.room


class Department(models.Model):
    faculty = models.ManyToManyField(FacultyMember)
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50, default="")
    location = models.ForeignKey(Location)
    budget = models.IntegerField(default=0)
    chairperson = models.ForeignKey(FacultyMember, related_name='+')

    def __unicode__(self):
        return self.code + " - " + self.name


class Student(models.Model):
    ssn = models.CharField(max_length=9)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    high_school = models.CharField(max_length=50)
    major = models.ForeignKey(Department)
    year = models.CharField(max_length=4)

    def __unicode__(self):
        return self.first_name + " " + self.last_name + " (" + self.ssn + ")"

    def clean(self):
        if (self.section_set.count() > 6):
            raise ValidationError('Students cannot register for more than 6 classes')


class TeachingAssistantStatus(models.Model):
    status = models.CharField(max_length=20, default="Full Time")

    class Meta:
        verbose_name_plural = "Teaching assistant statuses"

    def __unicode__(self):
        return self.status


class TeachingAssistant(models.Model):
    student = models.ForeignKey(Student)
    staff = models.ForeignKey(StaffMember)
    hours = models.IntegerField(default=0)
    status = models.ForeignKey(TeachingAssistantStatus)

    def __unicode__(self):
        return self.staff.first_name + " " + self.staff.last_name + " (" + self.staff.ssn + ")"

    # enforce hours
    def clean(self):
        if (self.status == "Full time") and (self.hours > 20):
            raise ValidationError('Full time Teaching Assistants cannot work more than 20 hours')
        elif (self.status == "Part Time") and (self.hours > 12):
            raise ValidationError('Part time Teaching Assistants cannot work more than 12 hours')
        else:
            raise ValidationError('Invalid input for Teaching Assistant hours')

    # clean to assert staff ssn = student ssn, as well as first and last name
    def clean(self):
        if (self.student.ssn != self.staff.ssn) and (self.student.first_name != self.staff.first_name) and (self.student.last_name != self.staff.last_name):
            raise ValidationError('Teaching Assistants must be registered first as both a student and a staff member')


class Course(models.Model):
    department = models.ForeignKey(Department)
    number = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    credit = models.IntegerField(default=0)
    ta_requirement = models.IntegerField(default=0)

    def __unicode__(self):
        return self.department.code + " " + self.number + " - " + self.name + " (" + str(self.credit) + " credits)"


class TimeSlot(models.Model):
    day = models.CharField(max_length=10)
    time = models.CharField(max_length=20)

    def __unicode__(self):
        return "(" + self.day[:3] + ": " + self.time + ")"

class Section(models.Model):
    course = models.ForeignKey(Course)
    number = models.CharField(max_length=5)
    location = models.ForeignKey(Location)
    time_slot = models.ManyToManyField(TimeSlot)
    max_enrollment = models.IntegerField(default=0)
    faculty = models.ForeignKey(FacultyMember)
    student = models.ManyToManyField(Student)
    teaching_assistant = models.ForeignKey(TeachingAssistant)

    def __unicode__(self):
        return self.course.department.code + " " + self.course.number + " - Section: " + self.number

    def clean(self):

        # enforce courseload on faculty
        # if (self.faculty.section.count() > self.faculty.course_load):
        #     raise ValidationError('Faculty member course load exceeded')

        # enforce max enrollment
        if (self.student.count() > self.max_enrollment):
            raise ValidationError('Class section is full')

        # enforce max number of sections a student can enroll in
        for student in self.student.all():
            student.clean()

        # # enforce course ta_requirement
        # if (self.course.ta_requirement_set.object.count > self.teaching_assistant.hours):
        #     raise ValidationError('Teaching Assistant hours exceeded for course TA requirement')

        # # enforce no more than two time_slots
        if (self.time_slot.count() > 2):
            raise ValidationError('Classes may be held no more than two times per week')

        # enforce room capacity
        if (self.location.capacity < self.max_enrollment):
            raise ValidationError('Max enrollment allowed for this section exceeds room capacity')
