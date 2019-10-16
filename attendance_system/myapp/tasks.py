from .get_employees import GetEmployees
from .download_excel import DownloadExcel
from attendance_system.celery import app
from .email import Email

@app.task()
def celery_excelGenerator():
    output =''
    employee_list = GetEmployees().get_employee_details()
    output = DownloadExcel().download_excel(employee_list)
    Email().send_attachment()