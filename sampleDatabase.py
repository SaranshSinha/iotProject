#expense=ent,utility,food,others
#income=sal,bonus,gift,cashback
import sqlite3
li=[['saransh','pizza','food','expense',200,'20/11/2019',1000],
['saransh','movie','entertainment','expense',300,'22/11/2019',1000],
['saransh','bill','utility','expense',500,'02/11/2019',2000],
['saransh','salary','salary','income',10000,'01/11/2019',0],
['saransh','diwali bonus','bonus','income',2000,'28/11/2019',0],
['saransh','amazonPay','cashback','income',100,'25/11/2019',0]]
conn=sqlite3.connect("ExpenseTracker2.db")
print("opened database successfully!")
try:
    conn.execute('''CREATE TABLE IF NOT EXISTS Expense
    (username CHAR(10)  NOT NULL,
    item CHAR(20) NOT NULL,
    tag TEXT NOT NULL,
    type TEXT NOT NULL,
    amount INT ,
    edate CHAR(10),
    lim INT
    );''')

except:
    print()

print("Table created successfully")
#conn.execute("""INSERT INTO Expense
#VALUES ('saransh', 'pizza','food', 'expense',100, date('now'),0 );""")
#print("data inserted successfully!")
for i in li:
    conn.execute("""INSERT INTO Expense VALUES(?,?,?,?,?,?,?);""",i)
print("data entry successful!")

conn.commit()
print("now showing the data: ")
cursor = conn.execute("SELECT * from Expense")

for row in cursor:

    print("NAME = ", row[0])

    print("ITEM = ", row[1])

    print("CATEGORY = ", row[2])

    print("TYPE = ", row[3])
    print("AMOUNT = ", row[4])
    print("DATE = ", row[5])
    print("LIMIT = ", row[6])
    
print("everything is working fine so far!")
conn.close()
