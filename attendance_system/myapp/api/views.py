from ..DBConnect import connect_to_db
from ..get_employees import GetEmployees
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response

class EmployeeListView(generics.ListAPIView):
    # cursor = connect_to_db()
    employees = GetEmployees().get_employee_details()
    # queryset = cursor.execute('SELECT * FROM Employee')
    # serializer_class = serializers.EmployeeSerializer