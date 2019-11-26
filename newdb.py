
#Ecat=["Entertainment","Utility","Education","Others"]
#Icat=["Salary","Bonus","Gift Income","Pension"]
import sqlite3
li=[['saransh','pizza','others','expense',200,'2019/11/03'],
['saransh','movie','entertainment','expense',300,'2019/11/22'],
['saransh','old age','pension','income',1000,'2019/11/25'],
['saransh','bill','utilities','expense',500,'2019/10/02'],
['saransh','diwali','gift income','income',500,'2019/10/02'],
['saransh','salary','salary','income',10000,'2019/09/01'],
['saransh','child edu','Education','expense',5000,'2019/09/01'],
['saransh','bonus','bonus','income',2000,'2019/08/28'],
['saransh','other','others','expense',1000,'2019/08/28']]
conn=sqlite3.connect("ExpenseTracker.db")
print("opened database successfully!")
try:
    conn.execute(CREATE TABLE IF NOT EXISTS Expense
    (username CHAR(10)  NOT NULL,
    item CHAR(20) NOT NULL,
    tag TEXT NOT NULL,
    type TEXT NOT NULL,
    amount INT ,
    edate CHAR(10)
    )
except:
    print()
print("Table created successfully")
#conn.execute("""INSERT INTO Expense
#VALUES ('saransh', 'pizza','food', 'expense',100, date('now'),0 );""")
#print("data inserted successfully!")
for i in li:
    conn.execute("""INSERT INTO Expense VALUES(?,?,?,?,?,?);""",i)
print("data entry successful!")
conn.commit()
print("now showing the data: ")'''
conn=sqlite3.connect("ExpenseTracker.db")
cursor = conn.execute("SELECT * from Expense")

for row in cursor:
    print("NAME = ", row[0])
    print("ITEM = ", row[1])
    print("CATEGORY = ", row[2])
    print("TYPE = ", row[3])
    print("AMOUNT = ", row[4])
    print("DATE = ", row[5])
print("everything is working fine so far!")
conn.close()
