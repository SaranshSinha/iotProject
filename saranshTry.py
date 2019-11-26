 conn.execute('''CREATE TABLE IF NOT EXISTS User
    (
    username CHAR(20) NOT NULL,
    passwrod CHAR(20) NOT NULL,
    budget INT NOT NULL
    );''')
