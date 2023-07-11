#from django.shortcuts import render
from django.views import View
from .models import Employee
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

class EmployeeView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, id=0):
        
        if (id > 0 ):
            employees = list(Employee.objects.filter(id=id).values())
            if len(employees) > 0:
                employee = employees[0]
                datos = {'message':"Success", 'employee': employee}
            else:
                datos = {'message': "Company not found"}
            return JsonResponse(datos)
        else:
            employees = list(Employee.objects.values())
            if len(employees) > 0:
                datos = {'message': "Success", 'employees': employees}
            else:
                datos = {'message': "Employees not fund"}
            return JsonResponse(datos)
    
    def post(self, request):
        #print(request.body)
        #json_data 
        jd= json.loads(request.body)
        
        Employee.objects.create(first_name=jd['first_name'], last_name=jd['last_name'], gender=jd['gender'],
                                email=jd['email'],job_title=jd['job_title'],department=jd['department'],
                                date_joined=jd['date_joined'],is_active=jd['is_active'])
        
        datos = {'message': 'Success'}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd= json.loads(request.body)
        employees = list(Employee.objects.filter(id=id).values())
        if len(employees)>0:
            employee = Employee.objects.get(id=id)
            employee.first_name = jd['first_name']
            employee.last_name = jd['last_name']
            employee.gender = jd['gender']
            employee.email = jd['email']
            employee.department = jd['department']
            employee.date_joined = jd['date_joined']
            employee.is_active = jd['is_active']
            employee.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Employee not fund"}
        return JsonResponse(datos)
        
    def delete(self, request, id):
        employees = list(Employee.objects.filter(id=id).values())
        if len(employees)>0:
            Employee.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Employee not fund"}
        return JsonResponse(datos)