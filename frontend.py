from tkinter import *
import backend

window = Tk()

input_name = StringVar()
input_author = StringVar()
input_year = StringVar()
input_isbn = StringVar()
error_message = StringVar()
selected_tuple = None


def get_selected_row(event):
    global selected_tuple
    clean_error()
    clean_input()
    index = l1.curselection()[0]
    selected_tuple = l1.get(index)
    e1.insert(END, selected_tuple[1])
    e2.insert(END, selected_tuple[2])
    e3.insert(END, selected_tuple[3])
    e4.insert(END, selected_tuple[4])


def close_button():
    backend.close_book()
    window.destroy()


def view_button():
    clean_input()
    l1.delete(0, END)
    for row in backend.view_books():
        l1.insert(END, row)


def clean_error():
    error_message.set("")


def clean_input():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


def clear_button():
    clean_input()
    clean_error()


def add_button():
    error_message.set(backend.add_book(
        e1.get(),
        e2.get(),
        e3.get(),
        e4.get()
    ))
    clean_input()
    view_button()


def delete_button():
    global selected_tuple
    index = l1.curselection()[0]
    selected_tuple = l1.get(index)
    backend.delete_book(str(selected_tuple[0]))
    view_button()


def update_button():
    global selected_tuple
    index = l1.curselection()[0]
    selected_tuple = l1.get(index)
    error_message.set(backend.update_book_by_id(
        selected_tuple[0],
        e1.get(),
        e2.get(),
        e3.get(),
        e4.get()))
    view_button()


def find_button():
    l1.delete(0, END)
    for row in backend.find_book(e1.get(),
                                 e2.get(),
                                 e3.get(),
                                 e4.get()):
        l1.insert(END, row)


t1 = Label(window, text="Name")
t1.grid(row=0, column=0)

e1 = Entry(window, textvariable=input_name)
e1.grid(row=0, column=1)

t2 = Label(window, text="Author")
t2.grid(row=0, column=2)

e2 = Entry(window, textvariable=input_author)
e2.grid(row=0, column=3)

t3 = Label(window, text="Year")
t3.grid(row=1, column=0)

e3 = Entry(window, textvariable=input_year)
e3.grid(row=1, column=1)

t4 = Label(window, text="ISBN")
t4.grid(row=1, column=2)

e4 = Entry(window, textvariable=input_isbn)
e4.grid(row=1, column=3)

bc = Button(window, width=10, text="Clear", command=clear_button)
bc.grid(row=2, column=3)

b1 = Button(window, width=10, text="ADD", command=add_button)
b1.grid(row=3, column=3)

b2 = Button(window, width=10, text="View all", command=view_button)
b2.grid(row=4, column=3)

b3 = Button(window, width=10, text="Find", command=find_button)
b3.grid(row=5, column=3)

b4 = Button(window, width=10, text="Update", command=update_button)
b4.grid(row=6, column=3)

b5 = Button(window, width=10, text="Delete", command=delete_button)
b5.grid(row=7, column=3)

b6 = Button(window, width=10, text="Close", command=close_button)
b6.grid(row=8, column=3)

err = Label(window, textvariable=error_message)
err.grid(row=2, column=0, columnspan=3)

l1 = Listbox(window, width=40)
l1.grid(row=3, column=0, columnspan=2, rowspan=6)
sb = Scrollbar(window)
sb.grid(row=3, column=2, rowspan=6)
l1.configure(yscrollcommand=sb.set)
sb.configure(command=l1.yview)
l1.bind('<<ListboxSelect>>', get_selected_row)

window.mainloop()
