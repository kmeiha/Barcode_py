import tkinter as tk
import tkinter.font as tkFont
import sqlite3
import os
import random
from barcode import EAN13
import barcode
from barcode.writer import ImageWriter
connection = sqlite3.connect("nice.db")  
cur = connection.cursor()
class App:
    def __init__(self, root):
        #setting title
        root.title("Barcode System")
        #setting window size
        width=404
        height=274
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_11=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_11["font"] = ft
        GLabel_11["fg"] = "#333333"
        GLabel_11["justify"] = "center"
        GLabel_11["text"] = "ID:"
        GLabel_11.place(x=30,y=40,width=70,height=25)

        global GLineEdit_655
        GLineEdit_655=tk.Entry(root)
        GLineEdit_655["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_655["font"] = ft
        GLineEdit_655["fg"] = "#333333"
        GLineEdit_655["justify"] = "center"
        GLineEdit_655["text"] = "ID"
        GLineEdit_655.place(x=100,y=40,width=70,height=25)

        GLabel_806=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_806["font"] = ft
        GLabel_806["fg"] = "#333333"
        GLabel_806["justify"] = "center"
        GLabel_806["text"] = "Name:"
        GLabel_806.place(x=20,y=80,width=70,height=25)

        global GLineEdit_981
        GLineEdit_981=tk.Entry(root)
        GLineEdit_981["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_981["font"] = ft
        GLineEdit_981["fg"] = "#333333"
        GLineEdit_981["justify"] = "center"
        GLineEdit_981["text"] = "Name"
        GLineEdit_981.place(x=100,y=80,width=70,height=25)

        GLabel_332=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_332["font"] = ft
        GLabel_332["fg"] = "#333333"
        GLabel_332["justify"] = "center"
        GLabel_332["text"] = "DPT:"
        GLabel_332.place(x=20,y=120,width=70,height=25)

        global GCheckBox_481
        GCheckBox_481=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_481["font"] = ft
        GCheckBox_481["fg"] = "#333333"
        GCheckBox_481["justify"] = "center"
        GCheckBox_481["text"] = "Open Barcode"
        GCheckBox_481.place(x=30,y=150,width=106,height=48)
        GCheckBox_481["offvalue"] = "0"
        GCheckBox_481["onvalue"] = "1"
        GCheckBox_481["command"] = self.GCheckBox_481_command

        global GLineEdit_901
        GLineEdit_901=tk.Entry(root)
        GLineEdit_901["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_901["font"] = ft
        GLineEdit_901["fg"] = "#333333"
        GLineEdit_901["justify"] = "center"
        GLineEdit_901["text"] = "DPT"
        GLineEdit_901.place(x=100,y=120,width=70,height=25)

        global GListBox_624
        GListBox_624 = tk.Listbox(root)
        GListBox_624["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_624["font"] = ft
        GListBox_624["fg"] = "#333333"
        GListBox_624["justify"] = "center"
        GListBox_624.place(x=210,y=40,width=127,height=112)

        GButton_687=tk.Button(root)
        GButton_687["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_687["font"] = ft
        GButton_687["fg"] = "#000000"
        GButton_687["justify"] = "center"
        GButton_687["text"] = "Update LIst"
        GButton_687.place(x=210,y=170,width=129,height=30)
        GButton_687["command"] = self.GButton_687_command

        GButton_522=tk.Button(root)
        GButton_522["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_522["font"] = ft
        GButton_522["fg"] = "#000000"
        GButton_522["justify"] = "center"
        GButton_522["text"] = "Create"
        GButton_522.place(x=120,y=210,width=70,height=25)
        GButton_522["command"] = self.GButton_522_command

        GButton_569=tk.Button(root)
        GButton_569["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_569["font"] = ft
        GButton_569["fg"] = "#000000"
        GButton_569["justify"] = "center"
        GButton_569["text"] = "Exit"
        GButton_569.place(x=20,y=210,width=70,height=25)
        GButton_569["command"] = self.GButton_569_command

    def GCheckBox_481_command(self):
        global image_name
        global checkboxva
        if GCheckBox_481.get() == 1:  # If checked open image
            os.startfile('Barcode_images\%s.svg' % image_name)

    def populatebox(self):
            GListBox_624.delete(0)
            sql_select_Query = "select id,name,type from main_table"
            first =  cur.execute(sql_select_Query)
            GListBox_624.commit()
            for i in first:
                GListBox_624.insert("end", i)
    
    def GButton_687_command(self):
        pass


    def GButton_522_command(self):
        def barecode(self):
            global image_name
            global ID
            global current_var
            ID_name = GLineEdit_981.get()
            ID = GLineEdit_655.get()
            ID_Dpt = GLineEdit_901.get()

            def validate():
                global ID
                ID = GLineEdit_655.get()
                ID_len = len(ID)
                if ID_len == 0:
                    ID = random.randint(100000000000, 999999999999)
            validate()
            ID = int(ID)
            #################################################################
            insert_data = "INSERT INTO main_table (id, name, dpt) VALUES (?, ?, ?)"
            val = (ID, ID_name, ID_Dpt)
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
            def image_opener(self):
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



    def GButton_569_command(self):
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
