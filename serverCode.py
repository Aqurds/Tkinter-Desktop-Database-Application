import sqlite3


# Function for creating database & table
def create_table():
    conn = sqlite3.connect('classRoom.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS classRoom (name TEXT, roll INTEGER, section TEXT, grade TEXT)")
    conn.commit()
    conn.close()
create_table()


# Function for inserting data to database
def insert(name, roll, section, grade):
    conn = sqlite3.connect('classRoom.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO classRoom VALUES(?,?,?,?)", (name, roll, section, grade))
    conn.commit()
    conn.close()


# Function to fetch all record from database
def view():
    conn = sqlite3.connect('classRoom.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM classRoom")
    data = cur.fetchall()
    conn.close()
    return data


# Function for searching a specific student record
def search(studentname):
    conn = sqlite3.connect('classRoom.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM classRoom WHERE name=?", (studentname,))
    data = cur.fetchall()
    conn.commit()
    conn.close()
    return data


# Function for deleting a specific student record
def delete(studentname):
    conn = sqlite3.connect('classRoom.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM classRoom WHERE name=?", (studentname,))
    data = cur.fetchall()
    conn.commit()
    conn.close()


# Function for updating a specific student record
def update(name, roll, section, grade):
    conn = sqlite3.connect('classRoom.db')
    cur = conn.cursor()
    cur.execute("UPDATE classRoom SET roll=?, section=?, grade=? WHERE name=?", (roll, section, grade, name))
    conn.commit()
    conn.close()
