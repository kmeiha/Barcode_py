import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("About")
        #setting window size
        width=800
        height=432
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_887=tk.Label(root)
        ft = tkFont.Font(family='Times',size=46)
        GLabel_887["font"] = ft
        GLabel_887["fg"] = "#333333"
        GLabel_887["justify"] = "center"
        GLabel_887["text"] = "This Project is made by"
        GLabel_887.place(x=0,y=40,width=675,height=190)

        GLabel_845=tk.Label(root)
        ft = tkFont.Font(family='Times',size=46)
        GLabel_845["font"] = ft
        GLabel_845["fg"] = "#333333"
        GLabel_845["justify"] = "center"
        GLabel_845["text"] = "KMEIHA"
        GLabel_845.place(x=480,y=260,width=294,height=125)
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
