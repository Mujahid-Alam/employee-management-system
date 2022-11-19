from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def home(request):
    isActive=True
    if request.method=='POST':
        c = request.POST.get('name')
        e = request.POST.get('email')
        if c is None : isActive=False
        else:isActive=True
        print(c)
        print(e)
    date = datetime.today()
    name = 'Mujahid Alam'
    student_list = [
        'arbaz',
        'Amin',
        'sumair',
        'Hashir'
    ]
    college_dict={
        'student_name':'Mujahid Alam',
        'college':'VVIT Purnia',
        'Mobile': 9507008132
    }
    data = {
        'date':date,
        'name':name,
        'student_list':student_list,
        'college_data':college_dict,
        'isActive':isActive,
    }
    return render(request, 'home.html', data)


def about(request):
    return render(request, 'about.html', {})

