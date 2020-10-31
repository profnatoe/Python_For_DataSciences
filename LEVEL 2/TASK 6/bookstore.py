import sqlite3
from sqlite3 import Error

def menu():
    
    #Defines the database then print-out the menu
    createDatabase()
    print("\n\nPulling database catalog.....")
    viewAllBooks()
    print("\n\n")
    while True:
        print("Welcome to eBookStore")
        print("==========================")
        print("\nMake a Selection Below: ")
        print("\n1) Enter a book")
        print("2) Update book")
        print("3) Delete book")
        print("4) Search Books")
        print("0) Exit")

                
        choice = int((input("Enter Your Choice: ")))
        
        if choice == 1:
            addBook()
            viewAllBooks()
        elif choice == 2:
            updateBook()
            viewAllBooks()
        elif choice == 3:
            viewAllBooks()
            book_id = input("\nEnter Book Id to delete: ")
            deleteBook(book_id)
            viewAllBooks()
        elif choice == 4:
            title = input("Enter Book title to search: ")
            searchBook(title)
        elif choice == 0:
            print("Thank You for using this application!")
            break

def databaseConnection():
    db = sqlite3.connect('ebookstore')
    return db

def createDatabase():
    connection = databaseConnection()
    cursor = connection.cursor()
    try:
        #cursor.execute('''DROP TABLE books''') #Destroy the entire database
        #connection.commit() # save changes we have made
        cursor.execute('''CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title TEXT, author TEXT, qty INTEGER)''')
        connection.commit()
       

    except Error as e:
        print("Cannot connect, see datails: ", e)
    finally:
        connection.close()


def addBook():
    b_title = input("Enter Book Title: ")
    b_author = input("Enter Book Author: ")
    b_qty = int(input("Enter Book Quantity: "))

   
    connection = databaseConnection()
    try:
        cursor = connection.cursor()
        #since the primary key auto increments I decided to leave it out so that the system can generate it for me
        cursor.execute('''INSERT INTO books(title, author, qty) VALUES(?,?,?)''', (b_title, b_author, b_qty))
        connection.commit()
        print("Book added successfully!")
        # cursor.execute('''SELECT * FROM books WHERE title = ?''', (b_title))
        #print(cursor.fetchmany())
    except Error as e:
        print("Cannot add book, see details: ", e)
        connection.rollback()
    finally:
        connection.close()

def updateBook():
    b_title_old = input("Enter existing Book Title from the Catalog: ")
    b_title = input("Enter New Book Title: ")
    b_author = input("Enter New Book Author: ")
    b_qty = input("Enter New Book Quantity: ")

    connection = databaseConnection()
    cursor = connection.cursor()

    try:
        cursor.execute('''
            UPDATE books
            SET title = ?, author = ?, qty = ?
            WHERE title = ?
            ''',
            (b_title, b_author, b_qty,b_title_old))
        connection.commit()
    except Error as e:
        connection.rollback()
        print(e)
    finally:
        connection.close()


def searchBook(book_title):

    connection = databaseConnection()
    cursor = connection.cursor()
    try:

        cursor.execute(
            f'''
            SELECT * FROM books WHERE title = ?
            ''', 
            (book_title,))
        print("=========\n\nSearch Completed:")
        print("The following Books were Retrived with the keyword: ", book_title)
        print("\n")
        for r in cursor.fetchall():
            print(r)
        print("\n====================\n")
    except Error as e:
        print(e)
    finally:
        connection.close()
def deleteBook(book_id):
    connection = databaseConnection()
    cursor = connection.cursor()
    cursor.execute('''DELETE FROM books WHERE id = ?''', (book_id))
    connection.commit()
    print("\nDeleted Successfully!")

def viewAllBooks():
    print("\n=======View eBookStore Catalog========\n\n")
    print("Book ID, Book Title, Book Author, Book Quantity:\n\n")
    connection = databaseConnection()
    cursor = connection.cursor()
    cursor.execute(f'''SELECT * FROM books''')
    for row in cursor.fetchall():
        print(row)
        
    print("\n============================\n")

if __name__ == "__main__":
    menu()