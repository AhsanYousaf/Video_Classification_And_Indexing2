from tkinter import *
from tkinter import messagebox
import pymysql

root=Tk()
class Main_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500")
        self.root.resizable(False,False)
        self.root.configure(background="black")
        self.root.title("Main_App")
        btn_bar=Frame(root,width=500,highlightbackground='white',height='40').place(x='0',y='5')
        Frame.txt_name = Entry(root)
        Frame.txt_name.place(x=300, y=12)
        btn_search = Button(root, text='search', width=8, bg='black', fg='white', command=self.search).place(x=430, y=9)
        btn_upload =Button(root, text='upload', width=8, bg='black', fg='white', command=self.upload).place(x=230, y=9)
        btn_logout = Button(root, text='Logout', width=8, bg='black', fg='white', command=self.logout).place(x=5, y=9)
        video_box = Frame(root, width=400, highlightbackground='white', height='300').place(x='50', y='100')
        btn_next = Button(root, text='>', width=4, bg='black', fg='white', command=self.next).place(x=250, y=450)
        btn_back = Button(root, text='<', width=4, bg='black', fg='white', command=self.back).place(x=210, y=450)

    def search(self):
        messagebox.showinfo("search", "we are searching here", parent=self.root)
    def upload(self):

        upload= Tk()
        upload.geometry("400x200")
        upload.resizable(False, False)
        upload.configure(background="black")
        upload.title("upload")
        btn_bar = Frame(upload, width=150, highlightbackground='white', height='100').place(x='20', y='10')
        title = Label(upload, text="Title", width=20, font=("bold", 10), bg="black", fg='grey')
        title.place(x=200, y=40)
        self.txt_name = Entry(upload).place(x=200, y=40)

        btn_browse = Button(upload, text='Browse', width=8, bg='grey', fg='black', command=self.up_done).place(x=200, y=80)
        btn_Uplaod = Button(upload, text='upload', width=8, bg='grey', fg='black', command=self.browse).place(x=60, y=130)
    def up_done(self):
        messagebox.showinfo("upload", "upload sucessfuly", parent=self.root)

    def browse(self):
        messagebox.showinfo("browse", "Browsing", parent=self.root)
    def logout(self):
         messagebox.showinfo("logout", "doing logout", parent=self.root)
    def next(self):
        messagebox.showinfo("next", "move to next video", parent=self.root)
    def back(self):
        messagebox.showinfo("back", "go to previous video", parent=self.root)
obj = Main_App(root)
root.mainloop()
