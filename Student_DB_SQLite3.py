import sqlite3

try:
    db = sqlite3.connect("student_db")

    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS
                        students(id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL ON CONFLICT IGNORE,
                                    grade INTEGER)""")
    
    db.commit()

    python_grades = [(10, "James Davis", 77), (55, "Janice smith", 80), (34, "Mark Harris", 67)]

    cursor.executemany("""INSERT OR REPLACE INTO students(id, name, grade)
                         VALUES(?,?,?)""", python_grades)
    
    db.commit()
    
    cursor.execute("""SELECT * FROM students""")

    for row in cursor:
        print(f"Student: {row[0]} Name: {row[1]} Grade: {row[2]}")

except Exception as error_msg:
    db.rollback()
    raise error_msg

finally:
    db.close()