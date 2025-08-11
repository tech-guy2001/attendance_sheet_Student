from django.shortcuts import render
from django.contrib import messages
from .models import Students,attendance

from django.http import HttpResponse
from openpyxl import Workbook
from .models import Students

# Create your views here.



# views.py
from django.shortcuts import render, redirect
from .forms import StudentForm,Student
from .utils import push_to_google_sheet,push_to_google_sheet_student,push_to_google_sheet_addence
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, login, logout
from django.contrib.auth.decorators import login_required
import random

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            # Push to Google Sheet
            push_to_google_sheet([student.id, student.name, student.email, student.marks])
            messages.success(request, 'wellcome to ipcs ...')
            return render(request, 'add_student.html')  # Optional success page
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'addstudent.html')


# add student....................................
def add_students(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        join_date = request.POST.get('join_date')
        contact_number = request.POST.get('contact_number')
        course = request.POST.get('course')
        batch = request.POST.get('batch')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if Students.objects.filter(email=email).exists():
            messages.error(request, 'your account is already exists ...')
            return render(request, 'addstudent.html')

        else:
            student=  Students.objects.create(
                name=name,
                join_date=join_date,
                contact_number=contact_number,
                course=course,
                batch=batch,
                password=password,
                email=email
            )
        username=f'{name}{random.randint(100, 1000)}'
        user = User.objects.create_user(username=username, email=email, password=password)
        push_to_google_sheet_student([student.id, student.name, student.join_date,student.contact_number,student.course,student.batch,student.email])
        user.save()
        login(request, user)
        messages.success(request, 'wellcome to ipcs ...')
        return redirect(dashboard)  # replace with your desired success page

    return render(request, 'addstudent.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Change this to your main page after login
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


@login_required
def dashboard(request):
    s=Students.objects.filter(email=request.user.email).first()
    return render(request, 'student_dashboard.html',{"student":s})


def logout_view(request):
    logout(request)
    return redirect('login')

from datetime import date, datetime
def makeintime(request):
    name=request.GET.get("name")
    current_date = date.today()
    current_datetime = datetime.now()
    intime = current_datetime.strftime("%I:%M:%p")
    attendance.objects.create(name=name,dates=current_date,intime=intime,email=request.user.email)
    messages.success(request, 'Intime is marked ...')
    return redirect('dashboard')

def makeouttime(request):
    
    current_date = date.today()
    current_datetime = datetime.now()
    outtime = current_datetime.strftime("%I:%M:%p")
    staf=request.GET.get("staf")
    topic=request.GET.get("topic")
    attendance.objects.filter(email=request.user.email,dates=current_date).update(outtime=outtime,staff=staf,topic=topic)
    student=attendance.objects.filter(email=request.user.email,dates=current_date).first()

    push_to_google_sheet_addence([student.id, student.dates.strftime("%Y-%m-%d"), student.name,student.intime,student.outtime,student.topic,student.staff])
    messages.success(request, 'Out time is marked ...')
    return redirect('dashboard')


def export_students_excel(request):
    # Create workbook and sheet
    wb = Workbook()
    ws = wb.active
    ws.title = "Students"
    n=Students.objects.filter(email=request.user.email).first()
    ws.append(['Name',n.name])
    ws.append(['Course',n.course])

    # Header row
    ws.append(['ID', 'Date', 'In Time', 'Out Time', 'Topic', 'Staff', 'Duration (hours)'])

# Data rows
    for student in attendance.objects.filter(email=request.user.email):
        in_time_obj = datetime.strptime(student.intime, "%I:%M:%p").time()
        out_time_obj = datetime.strptime(student.outtime, "%I:%M:%p").time()
        in_datetime = datetime.combine(datetime.today(), in_time_obj)
        out_datetime = datetime.combine(datetime.today(), out_time_obj)
        # Calculate duration in hours (rounded to 2 decimal places)
        duration = out_datetime - in_datetime
        duration_hours = round(duration.total_seconds() / 3600, 2)
        ws.append([student.id, student.dates.strftime("%Y-%m-%d"),student.intime,student.outtime,student.topic,student.staff,duration_hours])

    # Set response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=students.xlsx'

    # Save to response
    wb.save(response)
    return response


def demo(request):
    import json
    with open("djangoseet-3d24e8c79dad.json") as f:
        creds = json.load(f)
    print('GOOGLE_CREDENTIALS=' + json.dumps(creds).replace('\n', '\\n'))


def location(request):
    return render(request,"location.html")


