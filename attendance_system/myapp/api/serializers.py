from ..DBConnect import connect_to_db
from rest_framework import serializers



class EmployeeSerializer(serializers.ModelSerializer):
    pass
    # class Meta:
        # cursor = connect_to_db()
        # model = cursor.execute('SELECT * FROM Employee')
        # fields = ('empid', 'name', 'email')