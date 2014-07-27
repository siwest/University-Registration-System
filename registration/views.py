from django.shortcuts import render, get_list_or_404, get_object_or_404

# Create your views here.
from django.http import HttpResponse

from registration.models import Student, Department, Course, Section

# def index(request):
#     return HttpResponse("Welcome to the student registration index.")



def index(request):
    latest_student_list = Student.objects.order_by('-last_name')[:31]
    output = ', '.join([s.last_name for s in latest_student_list])
    return HttpResponse(output)

# def studentregistration(request, student_id):
#     return HttpResponse("You're looking at student registration %s." % student_id)

def class_list(request):
    department_list = Department.objects.order_by('code')
    course_list = Course.objects.order_by('number')
    context = { 'department_list': department_list,
                'course_list': course_list, }
    return render(request, 'registration/class_list.html', context)

def department_list(request):
    department_list = Department.objects.order_by('name')
    context = { 'department_list': department_list, }
    return render(request, 'registration/department_list.html', context)

def course_list(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    course_list = get_list_or_404(Course.objects.order_by('number'), department=department)
    context = { 'course_list': course_list, }
    return render(request, 'registration/course_list.html', context)

def section_list(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    section_list = get_list_or_404(Section.objects.order_by('number'), course=course)
    context = { 'section_list': section_list, }
    return render(request, 'registration/section_list.html', context)

def student_list(request, section_id):
    section = get_object_or_404(Section, pk=section_id)
    student_list = get_list_or_404(Student.objects.order_by('last_name','first_name'), section=section)
    context = { 'student_list': student_list, }
    return render(request, 'registration/student_list.html', context)

def student_section(request, student_ssn):
    student = get_object_or_404(Student, ssn = student_ssn)
    context = { 'student': student }
    return render(request, 'registration/student_section.html', context)
