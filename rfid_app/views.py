from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.
@login_required(login_url='login')
def HomeView(request):
    return render(request, "home.html")

@login_required(login_url='login')
def groupView(request):
    mydata = Student.objects.values('group').distinct().order_by('group')
    template = loader.get_template('groups.html')
    context = {
        'mydata': mydata,
    }
    return HttpResponse(template.render(context, request))
@login_required(login_url='login')
def grView(request, gr):
    mydata = Student.objects.filter(group__startswith=gr)
    template = loader.get_template('group.html')
    context = {
        'mydata': mydata,
    }
    return HttpResponse(template.render(context, request))

@login_required
@login_required(login_url='login')
def studentsView(request):
    mydata = Student.objects.all()
    template = loader.get_template('students.html')
    context = {
        'mydata': mydata,
    }
    return HttpResponse(template.render(context, request))
@login_required(login_url='login')
def studentView(request, rfid):
    mydata = Attendance.objects.all().select_related('RFID', 'room_id').filter(RFID=rfid)
    template = loader.get_template('student.html')
    context = {
        'mydata': mydata,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def attendanceView(request):
    
    template = loader.get_template('att/attendances.html')
    context = {
        'attendances': Attendance.objects.all().select_related('RFID', 'room_id')
    }
    print('context->', context)
    # [
    #     {
    #         'student_name': '',
    #         'room_name': '',
    #         'time': ''

    #     }
    # ]
    return HttpResponse(template.render(context, request))
@login_required(login_url='login')
def RoomView(request):
    mydata = Room.objects.all()
    template = loader.get_template('rooms.html')
    context = {
        'mydata': mydata,
    }
    return HttpResponse(template.render(context, request))
@login_required(login_url='login')
def rnView(request, rn):
    attendances = Attendance.objects.all().select_related('RFID','room_id').filter(room_id = rn)
    template = loader.get_template('att/attendances.html')
    context = {
        'attendances': attendances,
    }
    return HttpResponse(template.render(context, request))

def my_form(request):
    searched = request.GET.get('searched')
    mydata = Student.objects.filter(Q(name__contains=searched) | Q(surname__icontains=searched) | Q(group__icontains=searched))
    return render(request, 'students.html', {'mydata': mydata})  