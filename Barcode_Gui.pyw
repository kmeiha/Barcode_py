#################################################################
import re
from tkinter import *
from tkinter import ttk
from unittest import result
from barcode import EAN13
import barcode
from barcode.writer import ImageWriter
import os
from tkinter import messagebox
import random
import sqlite3
#################################################################
image_name = ""
ID = "" 
root = Tk()
#################################################################
                    ###FULL SCREEN###
#screen_width = root.winfo_screenwidth()
#screen_height = root.winfo_screenheight()
#root.geometry("%dx%d" %(screen_width, screen_height)) 
#################################################################
root.geometry("630x630")
root.resizable(False, False)
root.title('Barcode System')
root.iconbitmap('icon.ico')
root.configure(bg="#15616D")
#################################################################
checkboxva = IntVar()  # value of checkboxes
current_var = StringVar()
ID_Type = current_var.get()
#################################################################
connection = sqlite3.connect("nice.db")  
cur = connection.cursor()
sql_command = """CREATE TABLE IF NOT EXISTS main_table (
                    id INT(3) Primary Key,
                    name CHAR, 
                    dpt CHAR,
                    type CHAR );"""
cur.execute(sql_command)
#################################################################
def donothing():
    pass 
#################################################################
def number_only(text):
    if str.isdigit(text):
        return True
    elif text == '':
        return True
    else:
        return False
#################################################################
Font_tuple = ("Comic Sans MS", 20, "bold",)
Font_tuple2 = ("Comic Sans MS", 20, "bold",)
choice = ['Pc', 'Laptop', 'Monitor', 'Keyboard',
            'Mouse', 'Printer', 'Phone', 'Other']
checkboxva = IntVar()
#################################################################
var = checkboxva.get  # value of checkboxes
#################################################################
reg_fun = root.register(number_only)
#################################################################
LabelName = Label(root, text="Name",
                    bg="#15616D", fg="#EADEDA", font=Font_tuple).place(x=20, y=30)
EntryName = Entry(root, bg="#d8f3dc", width=20,
                    validate='key')
EntryName.place(x=110, y=38)

labelId = Label(root, text="Id",
                    bg="#15616D", fg="#EADEDA", font=Font_tuple).place(x=20, y=125)
EntryId = Entry(root, bg="#d8f3dc", width=20, validate='key',
                    validatecommand=(reg_fun, '%P'))
EntryId.place(x=105, y=137)

labelType = Label(root, text="Type", bg="#15616D",
                    fg="#EADEDA", font=Font_tuple).place(x=20, y=215)
ChoicesType = ttk.Combobox(
        root, values=choice, textvariable=current_var, state="readonly").place(x=105, y=225)

LabelDpt = Label(root, text="Dpt.",
                    bg="#15616D", fg="#EADEDA", font=Font_tuple).place(x=20, y=300)
EntryDpt = Entry(root, bg="#d8f3dc", width=16)
EntryDpt.place(x=105, y=320)

checkbox1 = Checkbutton(root, text="Open image", font=Font_tuple2,
                            bg="#15616D", variable=checkboxva, onvalue=1, offvalue=0)
checkbox1.place(x=20, y=385)
#################################################################
ID = EntryId.get()
#################################################################
def barecode():
    global image_name
    global ID
    global current_var
    ID_name = EntryName.get()
    ID = EntryId.get()
    ID_Dpt = EntryDpt.get()
    ID_Type = current_var.get()

    def validate():
        global ID
        ID = EntryId.get()
        ID_len = len(ID)
        if ID_len == 0:
            ID = random.randint(100000000000, 999999999999)
    validate()
    ID = int(ID)
    #################################################################
    insert_data = "INSERT INTO main_table (id, name, dpt, type) VALUES (?, ?, ?, ?)"
    val = (ID, ID_name, ID_Dpt, ID_Type)
    cur.execute(insert_data, val)
    #################################################################
    ID = str(ID)
    ID = ID + '000000000'   #because it need 12 character
    #################################################################
    with open('backup_txt/backup_txt.txt', 'a', encoding='utf-8') as f:
        f.write('ID : ' + ID + '\t')
        f.write('Name: ' + ID_name + '\t') 
        f.write('Department: ' + ID_Dpt + '\n')
        f.close()
    #################################################################
    def csv_creator():
        pass
        #to do insert data in a csv file 
    #################################################################
    def json_creator():
        pass
        #to do insert data in to json
    #################################################################
    my_code = EAN13(ID)
    image_name =  ID + '_' + ID_name
    my_code.save('Barcode_images/%s' %image_name)
    #################################################################
    def image_opener():
        global image_name
        global checkboxva
        var = checkboxva.get()
        if var == 1:  # If checked open image
            os.startfile('Barcode_images\%s.svg' % image_name)
    #################################################################
    def print_image():
        pass 
        #to do print image with checkbox
    #################################################################
    image_opener()
    EntryName.delete(0, "end")
    EntryId.delete(0, "end")
    EntryDpt.delete(0, "end")
#################################################################
Create_btn = Button(root, text='Create', width=7, bg="#d8f3dc",
                        command=barecode).place(x=200, y=560)

Cancel_btn = Button(root, text='Cancel', width=7, bg="#d8f3dc",
                        command=root.destroy).place(x=20, y=560)
#################################################################
def populatebox():
    listBox.delete(0,END)
    sql_select_Query = "select id,name,type from main_table"
    first =  cur.execute(sql_select_Query)
    connection.commit()
    for i in first:
        listBox.insert("end", i)
#################################################################
listBox = Listbox(root)
listBox.pack()
btn = Button(root, text="Update list", command = lambda: populatebox())
btn.pack()
#################################################################
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
#################################################################
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help", command=donothing)
helpmenu.add_command(label="About", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)
#################################################################
root.mainloop()
connection.commit()
connection.close()
#################################################################