from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Emp
# Create your views here.
def emp_home(request):
    emps= Emp.objects.all()
    data = { 
        'emps':emps
    }
    return render(request, 'emp/home.html',data)

def add_emp(request):
    if request.method=='POST':
        #fetch data
        emp_name = request.POST.get('emp_name')     
        emp_id = request.POST.get('emp_id')
        emp_phone = request.POST.get('emp_phone')     
        emp_address= request.POST.get('emp_address')    
        emp_department = request.POST.get('emp_department')
        emp_working = request.POST.get('emp_working')

        # set data in objects
        e = Emp()
        e.name=emp_name
        e.employee_id=emp_id
        e.phone_no=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        #Save
        e.save()

        return redirect('/emp/home')
    return render(request, 'emp/add_emp.html', {})

def emp_delete(request, emp_id):
    emp = Emp.objects.get(id=emp_id)
    emp.delete()
    return redirect('/emp/home/')


def emp_update(request, emp_id):
    emp_up = Emp.objects.get(id=emp_id)
    data = {
        'emp_up':emp_up
    }
    return render(request, 'emp/update_emp.html', data)

def do_emp_update(request, emp_id):
    if request.method=='POST':
            #fetch data
        emp_name = request.POST.get('emp_name')     
        emp_id_temp = request.POST.get('emp_id')
        emp_phone = request.POST.get('emp_phone')     
        emp_address= request.POST.get('emp_address')    
        emp_department = request.POST.get('emp_department')
        emp_working = request.POST.get('emp_working')

        e = Emp.objects.get(id=emp_id)
        e.name=emp_name
        e.employee_id=emp_id_temp
        e.phone_no=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        #Save
        e.save()
    return redirect('/emp/home/')