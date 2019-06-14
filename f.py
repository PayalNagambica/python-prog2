#updating data in table


import sqlite3
conn=sqlite3.connect('table1.db')
print('opened database successfully')
cursor=conn.execute('update company set salary=25000.00 where id =1')
conn.commit()
print('total number of rows updated :',conn.total_changes)
cursor=conn.execute('''select id,name,salary from company''')
for row in cursor:
    print("id=",row[0])
    print("name=",row[1])
    print("salary=",row[2],"\n")
print("operation done successfully")
conn.close()