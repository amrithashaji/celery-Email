from .DBConnect import connect_to_db

class GetEmployees:

    def get_employee_details(self):
        employee_details = {}

        cursor = connect_to_db()
        cursor.execute('SELECT * FROM Employee')
        for row in cursor:
            emp = {}

            emp['name'] = row[1]
            emp['email'] = row[2]
            emp['time_from'] = row[4]
            emp['time_to'] = row[5]
            employee_details[row[0]] = emp
        return employee_details
        # print(employee_details)