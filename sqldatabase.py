import pyodbc


conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=LAPTOP-5818FKV9\SQLEXPRESS;'
                        'Database=QuizDB;'
                        'Trusted_Connection=Yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM Quiz')

for row in cursor:
    print(row)
