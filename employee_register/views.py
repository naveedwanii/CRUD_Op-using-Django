from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import EmployeeForm
from .models import Employee
from django.views import View

# Create your views here.
"""
def employee_list(request):
    context = {'employee_list':Employee.objects.all()}
    return render(request, "employee_register/employee_list.html",context)

def employee_form(request,id=0):
    if request.method == 'GET':
        if id==0:
           form = EmployeeForm()
        else:
           employee = Employee.objects.get(pk=id)
           form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html",{'form':form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance = employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')

def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('employee/list')

"""
class EmployeeList(View):
    def get(self,request):
        context = {'employee_list':Employee.objects.all()}
        return render(request, "employee_register/employee_list.html",context)

class EmployeeFormView(View):
    form_class = EmployeeForm
    initial = {'key': 'value'}
    template_name = 'employee_register/employee_form.html'

    def get(self, request, note_id=0, *args, **kwargs):
        if note_id == 0:
           form = self.form_class(initial = self.initial)
        else:
           employee = Employee.objects.get(pk=note_id)
           form = self.form_class(instance=employee)
        return render(request, self.template_name, {'form':form})

    def post(self, request , note_id=0, *args, **kwargs):
        if note_id  == 0:
            form = self.form_class(request.POST)
        else:
            employee = Employee.objects.get(pk=note_id)
            form = self.form_class(request.POST,instance = employee)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/list/')
            return render(request, self.template_name, {'form': form})



