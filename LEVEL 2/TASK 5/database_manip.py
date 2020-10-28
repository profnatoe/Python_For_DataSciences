import sqlite3

try:
    db = sqlite3.connect('python_programming')

    cursor = db.cursor()
    cursor.execute('''DROP TABLE python_programming''')
    db.commit()
    cursor.execute('''CREATE TABLE IF NOT EXISTS python_programming(id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)''')
    db.commit()



    id1 = 55
    name1 = 'Carl Davis'
    grade1 = 61

    id2 = 66
    name2 = 'Dennis Fredrickson' 
    grade2 = 88

    id3 = 77
    name3 = 'Jane Rcihards'
    grade3 = 78

    id4 = 12
    name4 = 'Peyton Sawyer'
    grade4 = 45

    id5 = 2
    name5 = 'Lucas Brooke'
    grade5 = 99

  
    cursor.execute('''INSERT INTO python_programming(id, name, grade)
        VALUES(?,?,?)''', (id1, name1, grade1))
    print('First user inserted')


    cursor.execute('''INSERT INTO python_programming(id, name, grade)
        VALUES(?,?,?)''', (id2, name2, grade2))
    print('second user inserted')


    cursor.execute('''INSERT INTO python_programming(id, name, grade)
        VALUES(?,?,?)''', (id3, name3, grade3))
    print('third user inserted')


    cursor.execute('''INSERT INTO python_programming(id, name, grade)
        VALUES(?,?,?)''', (id4, name4, grade4))
    print('fourth user inserted')


    cursor.execute('''INSERT INTO python_programming(id, name, grade)
        VALUES(?,?,?)''', (id5, name5, grade5))
    print('fifth user inserted')


    db.commit()

    cursor.execute('''SELECT * FROM python_programming''')
    print(cursor.fetchall())
    #Select record with grade between 60 and 80

    print("\n\n\n================\n\n Selecting with Where Clause Selection: \n\n\n\n")
    cursor.execute(
        '''
        SELECT * FROM python_programming
        WHERE grade BETWEEN 60 AND 80
        '''
        )

    print(cursor.fetchall())

    #change carl davis's grade to 65
    print("\n=====================\nChanging Carl Davis's grade:\n\n\n\n")
    cursor.execute(
        '''
        UPDATE python_programming
        SET grade = ?
        WHERE id = ?
        ''', (65,55))
    db.commit()
    cursor.execute('''SELECT * FROM python_programming''')
    print(cursor.fetchall())

    #delete Dennis Fredrickson's row
    print("==================\n\nDeleting Dennis Fredrickson: \n\n\n")
    cursor.execute('''DELETE FROM python_programming WHERE id = ? ''', (66,))
    db.commit()
    cursor.execute('''SELECT * FROM python_programming''')
    print(cursor.fetchall())


    #change the grade of all people with an id below than 55
    print("===================\n\nChanging grades \n\n\n")
    cursor.execute(
        '''
        UPDATE python_programming
        SET grade = 55
        WHERE id < 55
        ''')
    db.commit()
    cursor.execute('''SELECT * FROM python_programming''')
    print(cursor.fetchall())

except Except as e:
    db.rollback()
    raise e 
finally:
    db.close()

