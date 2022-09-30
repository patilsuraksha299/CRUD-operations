from django.shortcuts import render,redirect

from app.forms import EmployeeForm
from .forms import EmployeeForm
from .models import Employee

def employee_list(request):
    context={
        "employee_list":Employee.objects.all()
    }
    return render(request,"app/employee_list.html",context)

def employee_form(request,id=0):
    if request.method=="GET":
        if id == 0:     #insert operation 
            form=EmployeeForm()
        else:           #update operation
            employee=Employee.objects.get(pk=id)
            form=EmployeeForm(instance=employee)
        return render(request,"app/employee_form.html",{"form":form})
    else:       #when its a POST request
        if id==0:      #insert operation 
            form=EmployeeForm(request.POST)
        else:           #update operation
            employee=Employee.objects.get(pk=id)
            form=EmployeeForm(request.POST,instance=employee)
            
        if form.is_valid():
            form.save()
        return redirect('/app/list')


def employee_delete(request,id):
    employee=Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/app/list')