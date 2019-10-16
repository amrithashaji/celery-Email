def connect_to_db():
    import pyodbc
    server = 'SEZ-UWS-11'
    database = 'mydb'
    username = 'digitalmesh'
    password = 'password#1'
    con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=' + server + ';'
                          'DATABASE=' + database + ';'
                          'UID=' + username + ';'
                          'PWD=' + password)
    cursor = con.cursor()
    return cursor