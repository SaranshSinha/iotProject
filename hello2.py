import sqlite3
li=[['pizza', 300],['cigaratte',300],['OYO',1000]]
conn=sqlite3.connect("ExpenseTracker.db")
print("opened database successfully!")
try:
    conn.execute('''CREATE TABLE IF NOT EXISTS Budget

    (
    item CHAR(20) NOT NULL,
    lim INT
    );''')

except:
    print()

print("Table created successfully")
#conn.execute("""INSERT INTO Expense

#VALUES ('saransh', 'pizza','food', 'expense',100, date('now'),0 );""")
#print("data inserted successfully!")
for i in  li:
    conn.execute("""INSERT INTO Budget VALUES(?,?);""",i)

conn.commit()
print("now showing the data: ")
cursor = conn.execute("SELECT * from Budget")

for row in cursor:

    print("ITEM = ", row[0])

    print("LIMIT = ", row[1])
    print("------------")


print("everything is working fine so far!")
conn.close()
