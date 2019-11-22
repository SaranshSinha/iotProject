import sqlite3
#li=[6,'saransh',21,'Gujarat',10000.0]
conn=sqlite3.connect("ExpenseTracker.db")
print("opened database successfully!")
try:
    conn.execute('''CREATE TABLE IF NOT EXISTS Expense

    (username CHAR(10)  NOT NULL,

    item CHAR(20) NOT NULL,

    tag TEXT NOT NULL,

    type TEXT NOT NULL,

    amount INT ,

    edate DATE,
    lim INT
    );''')

except:
    print()

print("Table created successfully")
conn.execute("""INSERT INTO Expense

VALUES ('saransh', 'pizza','food', 'expense',100, date('now'),0 );""")
print("data inserted successfully!")
#conn.execute("""INSERT INTO COMPANY VALUES(?,?,?,?,?);""",li)

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
