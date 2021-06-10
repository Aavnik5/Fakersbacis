from django.shortcuts import render
from django.http import HttpResponse
from .helpers import *
from .models import *


# Create your views here.
def aavnik (request):
    generate_fake_data()
    student = Student.objects.all()
    return render(request,'home.html',{"student":student})
    

