from Backend import Database
from tkinter import *

database = Database("Bookrecords.db", "Books")

class Interface:
    
    def __init__(self, widget):
        self.window = widget
        self.window.wm_title("Book Store")

        self.l1 = Label(self.window, text="Title") 
        self.l1.grid(row=0, column=0)

        self.l2 = Label(self.window, text="Author") 
        self.l2.grid(row=0, column=3)

        self.l3 = Label(self.window, text="Year") 
        self.l3.grid(row=2, column=0)

        self.l4 = Label(self.window, text="ISBN") 
        self.l4.grid(row=2, column=3)

        self.e1_value = StringVar()
        self.e1 = Entry(self.window, textvariable=self.e1_value)
        self.e1.grid(row=0, column=1, columnspan=2)

        self.e2_value = StringVar()
        self.e2 = Entry(self.window, textvariable=self.e2_value)
        self.e2.grid(row=0, column=4, columnspan=2) 

        self.e3_value = StringVar()
        self.e3 = Entry(self.window, textvariable=self.e3_value)
        self.e3.grid(row=2, column=1, columnspan=2) 

        self.e4_value = StringVar()
        self.e4 = Entry(self.window, textvariable=self.e4_value)
        self.e4.grid(row=2, column=4, columnspan=2) 

        self.List_View = Listbox(self.window, height=15, width=30) 
        self.List_View.grid(row=3, column=0, rowspan=6, columnspan=4)
        self.List_View.bind('<<ListboxSelect>>', self.Fill_entry_boxes)

        scrollerv = Scrollbar(self.window)
        scrollerv.grid(row=3, column=4, rowspan=6)

        scrollerh = Scrollbar(self.window, orient=HORIZONTAL)
        scrollerh.grid(column=0, row=9, columnspan=4)

        self.List_View.configure(yscrollcommand=scrollerv.set, xscrollcommand=scrollerh.set)
        scrollerh.configure(command=self.List_View.xview)
        scrollerv.configure(command=self.List_View.yview)


        self.b1 = Button(self.window, text="View Records", command=self.view_records)
        self.b1.grid(row=3, column=5, columnspan=2)

        self.b2 = Button(self.window, text="Search Records", command=self.search_records)
        self.b2.grid(row=4, column=5, columnspan=2)

        self.b3 = Button(self.window, text="Update entry", command=self.update_entry)
        self.b3.grid(row=5, column=5, columnspan=2)

        self.b4 = Button(self.window, text="Delete entry", command=self.delete_entry)
        self.b4.grid(row=6, column=5, columnspan=2)

        self.b5 = Button(self.window, text="Add entry", command=self.new_entry)
        self.b5.grid(row=7, column=5, columnspan=2)

        self.b6 = Button(self.window, text="Close", command=self.window.quit)
        self.b6.grid(row=8, column=5, columnspan=2)


    def Fill_entry_boxes(self,Event): 
        global item
        index = self.List_View.curselection()[0]
        item = self.List_View.get(index)
        self.e1.delete(0, END)
        self.e1.insert(END, item[1])
        self.e2.delete(0, END)
        self.e2.insert(END, item[2])
        self.e3.delete(0, END)
        self.e3.insert(END, item[3])
        self.e4.delete(0, END)
        self.e4.insert(END, item[4])



    def view_records(self):
        self.List_View.delete(0, END)
        for row in database.view():
            self.List_View.insert(END, row)

    def search_records(self):
        if len(database.search(self.e1_value.get(), self.e2_value.get(), self.e3_value.get(), self.e4_value.get())) <= 0:
            self.List_View.delete(0, END)
            self.List_View.insert(END, "Sorry, entry not in records")
        else:
            self.List_View.delete(0, END)
            for row in database.search(self.e1_value.get(), self.e2_value.get(), self.e3_value.get(), self.e4_value.get()):
                self.List_View.insert(END, row)

    def delete_entry(self):
        database.delete(self.List_View.selection_get().split()[0])
        self.List_View.delete(0, END)
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.view_records()

    def new_entry(self):
        boxes =[self.e1_value.get(), self.e2_value.get(), self.e3_value.get(), self.e4_value.get()]
        if any(box == "" for box in boxes):
            self.List_View.insert(END, "Incomplete Details")
        else:
            database.insert(boxes[0], boxes[1], boxes[2], boxes[3])
            self.List_View.delete(0,END)
            self.view_records()

    def update_entry(self):
        database.update(item[0], self.e1_value.get(), self.e2_value.get(), self.e3_value.get(), self.e4_value.get())
        self.List_View.delete(0, END)
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.view_records()

window = Tk()
Interface(window)
window.mainloop()
