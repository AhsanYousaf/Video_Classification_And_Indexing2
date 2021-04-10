import os
from tkinter import *
from tkinter import messagebox, filedialog
from os import system
import cv2
import pymysql

root=Tk()
upload= Tk()


def spliting(filename):
    cam = cv2.VideoCapture(filename)

    try:

        # creating a folder named data
        if not os.path.exists('data'):
            os.makedirs('data')

        # if not created then raise error
    except OSError:
        print('Error: Creating directory of data')

    # frame
    currentframe = 0

    while (True):

        # reading from frame
        ret, frame = cam.read()

        if ret:
            # if video is still left continue creating images
            name = './data/frame' + str(currentframe) + '.jpg'
            print('Creating...' + name)

            # writing the extracted images
            cv2.imwrite(name, frame)

            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break

    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()


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
        btn_logout =Button(root, text='Logout', width=8, bg='black', fg='white', command=self.logout).place(x=5, y=9)
        video_box = Frame(root, width=400, highlightbackground='white', height='300').place(x='50', y='100')
        btn_next = Button(root, text='>', width=4, bg='black', fg='white', command=self.next).place(x=250, y=450)
        btn_back = Button(root, text='<', width=4, bg='black', fg='white', command=self.back).place(x=210, y=450)
#to search the user required category
    def search(self):
        messagebox.showinfo("search", "we are searching here", parent=self.root)


    def upload(self):
        filename = filedialog.askopenfilename(initialdir="/", title="select a file",
                                              filetype=(("mp4", "*.mp4"), ("All Files", "*.*")))
        if(filename!=""):
            spliting(filename)
            try:
                    connection = pymysql.connect(host="localhost", user="root", password="", database="db_connectivity")
                    cursor = connection.cursor()
                    cursor.execute("insert into video_db (video) values (%s)",(filename))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo("Success", "Successfuly upload", parent=upload)
                    # system('Main_App.py')
            except Exception as es:
                    messagebox.showerror("Error", f"Error due to:{str(es)}", parent=upload)

    def logout(self):
         messagebox.showinfo("logout", "doing logout", parent=self.root)
    def next(self):
        messagebox.showinfo("next", "move to next video", parent=self.root)
    def back(self):
        messagebox.showinfo("back", "go to previous video", parent=self.root)
obj = Main_App(root)
root.mainloop()
