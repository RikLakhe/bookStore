import sqlite3

con = sqlite3.connect("books.db")

cur = con.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS books 
    (book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
     author TEXT NOT NULL,
      year INTEGER NOT NULL,
       ISBN INTEGER NOT NULL)
    ''')
con.commit()


def add_book(name, author, year, isbn):
    try:
        cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)", (str(name), str(author), int(year), int(isbn)))
        con.commit()
        return None
    except:
        return ("Error in add.")


def view_books():
    cur.execute("SELECT * FROM books")
    row = cur.fetchall()
    return row


def find_book(name, author, year, isbn):
    cur.execute("SELECT * FROM books WHERE name=? OR author=? OR year=? OR isbn=?", (name, author, year, isbn))
    row = cur.fetchall()
    return row


def find_by_id(id):
    cur.execute("SELECT * FROM books WHERE book_id=?", (id))
    row = cur.fetchall()
    return row


def update_book_by_id(id, new_name, new_author, new_year, new_isbn):
    try:
        cur.execute("UPDATE books SET name=?, author=?, year=?,ISBN=? WHERE book_id=?",
                    (str(new_name), str(new_author), int(new_year), int(new_isbn), id))
        con.commit()
        return None
    except:
        return ("Error in add.")


def delete_book(id):
    cur.execute("DELETE FROM books WHERE book_id=?", (id))
    con.commit()


def close_book():
    cur.close()
