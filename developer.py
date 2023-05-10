from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import webbrowser
from time import strftime

class Developer:

    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Face Recognition System')

        # Making Title
        title_lbl = Label(self.root, text=" DEVELOPER INFORMATION  ", font=('times new roman', 30,
                          'bold'),
                          bg='black', fg='white')
        title_lbl.place(x=0, y=0, width=1530, height=53)

        # =============Time=======================================
        def time():
            String = strftime("%H:%M:%S %p")
            lbl.config(text=String)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=('times new roman', 20, 'bold'), bg='black', fg='yellow')
        lbl.place(x=0, y=0, width=220, height=50)
        time()

        # Background Image
        img1 = Image.open(r'college_images\bg4.png')
        img1 = img1.resize((1530, 720), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=50, width=1530, height=725)

        # Making Frame
        main_frame = Frame(f_lbl, bd=2, bg='black')
        main_frame.place(x=350, y=183, width=650, height=262)

        exit_btn = Button(title_lbl, text="Exit", command=self.exit, font=("times new roman", 12, "bold"),
                          bg='white', fg='black',
                          width=17)
        exit_btn.place(x=1200, y=3, width=120, height=42)

        # developer Image
        img2 = Image.open(r'college_images\IMG_20220525_172358_661.jpg')
        img2 = img2.resize((255, 260), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(main_frame, image=self.photoimg2, background='black')
        f_lbl2.place(x=333, y=5, width=325, height=250)

        # =================Linkedin====================
        linkedin_btn = Button(main_frame, text="Linkedin", command=self.linkedin, font=("times new roman", 20, "bold"),
                              bg='blue', fg='white',
                              width=500)
        linkedin_btn.place(x=80, y=5, width=242, height=58)

        img5 = Image.open(r'college_images\linkedin.png')
        img5 = img5.resize((70, 58), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        f_lbl5 = Label(main_frame, image=self.photoimg5, background='black')
        f_lbl5.place(x=5, y=7, width=62, height=52)

        # ======================Instagram==============
        insta_btn = Button(main_frame, text="Instagram", command=self.instagram, font=("times new roman", 20, "bold"),
                           bg='#e600e6', fg='white',
                           width=500)
        insta_btn.place(x=80, y=67, width=242, height=58)

        img4 = Image.open(r'college_images\insta_new.png')
        img4 = img4.resize((70, 58), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        f_lbl4 = Label(main_frame, image=self.photoimg4, background='black')
        f_lbl4.place(x=5, y=68, width=62, height=52)

        # ===================Email======================
        gmail_btn = Button(main_frame, text="E-mail", command=self.email, font=("times new roman", 20, "bold"),
                           bg='red', fg='white',
                           width=500)
        gmail_btn.place(x=80, y=129, width=242, height=58)

        img3 = Image.open(r'college_images\email.png')
        img3 = img3.resize((70, 58), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl3 = Label(main_frame, image=self.photoimg3, background='black')
        f_lbl3.place(x=5, y=133, width=62, height=52)

        # myname_btn = Button(main_frame, text="Aayush Upadhyay", font=("times new roman", 20, "bold"),
        #                       bg='dark blue', fg='white',
        #                       width=500)
        # myname_btn.place(x=0, y=192, width=332, height=60)

        name_lbl = Label(main_frame, text=" My name is Aayush Upadhyay ", font=('times new roman', 18, 'bold'),
                         bg='black', fg='white')
        name_lbl.place(x=0, y=192, width=332, height=60)

    def exit(self):
        choice = messagebox.askyesno("Exit", "Are you sure to Exit ? ", parent=self.root)
        if choice > 0:
            self.root.destroy()
        else:
            return

    def linkedin(self):
        self.new = 1
        self.url = "https://www.linkedin.com/in/aayush-upadhyay-010806216/"
        webbrowser.open(self.url, new=self.new)

    def instagram(self):
        self.new = 1
        self.url = "https://www.instagram.com/_au_since_2002/?next=%2F"
        webbrowser.open(self.url, new=self.new)

    def email(self):
        self.new = 1
        self.url = "https://mail.google.com/mail/u/0/#inbox"
        webbrowser.open(self.url, new=self.new)


if __name__ == '__main__':
    root = Tk()
    obj = Developer(root)
    root.mainloop()
