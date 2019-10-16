from django.shortcuts import render
from django.http.response import HttpResponse
from .get_employees import GetEmployees
from .download_excel import DownloadExcel
from .tasks import *


# Create your views here.
def index(request):
    employee_list = GetEmployees().get_employee_details()
    return render(request,'index.html',{'employee':employee_list,'flag':False})

def excelGenerator(request):
    output=celery_excelGenerator.delay()
    # employee_list = GetEmployees().get_employee_details()
    # output = DownloadExcel().download_excel(employee_list)
    return (output.task_id)


