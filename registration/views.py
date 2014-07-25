from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from registration.models import Student

# def index(request):
#     return HttpResponse("Welcome to the student registration index.")



def index(request):
    latest_student_list = Student.objects.order_by('-last_name')[:31]
    output = ', '.join([s.last_name for s in latest_student_list])
    return HttpResponse(output)

# def studentregistration(request, student_id):
#     return HttpResponse("You're looking at student registration %s." % student_id)
