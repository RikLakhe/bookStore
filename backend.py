import sqlite3


class Database:

    def __init__(self):
        self.con = sqlite3.connect("books.db")
        self.cur = self.con.cursor()
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS books 
            (book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
             author TEXT NOT NULL,
              year INTEGER NOT NULL,
               ISBN INTEGER NOT NULL)
            ''')
        self.con.commit()

    def add_book(self, name, author, year, isbn):
        try:
            self.cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)", (str(name), str(author), int(year), int(isbn)))
            self.con.commit()
            return None
        except:
            return ("Error in add.")

    def view_books(self):
        self.cur.execute("SELECT * FROM books")
        row = self.cur.fetchall()
        return row

    def find_book(self, name, author, year, isbn):
        self.cur.execute("SELECT * FROM books WHERE name=? OR author=? OR year=? OR isbn=?", (name, author, year, isbn))
        row = self.cur.fetchall()
        return row

    def find_by_id(self, id):
        self.cur.execute("SELECT * FROM books WHERE book_id=?", (id))
        row = self.cur.fetchall()
        return row

    def update_book_by_id(self, id, new_name, new_author, new_year, new_isbn):
        try:
            self.cur.execute("UPDATE books SET name=?, author=?, year=?,ISBN=? WHERE book_id=?",
                             (str(new_name), str(new_author), int(new_year), int(new_isbn), id))
            self.con.commit()
            return None
        except:
            return ("Error in add.")

    def delete_book(self, id):
        self.cur.execute("DELETE FROM books WHERE book_id=?", (id))
        self.con.commit()

    def __del__(self):
        self.cur.close()
