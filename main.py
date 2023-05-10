from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from student import Student
import cv2
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendances
from developer import Developer
from chatbot import ChatBot
from time import strftime
from datetime import datetime


class Face_Recognition_System:

    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Face Recognition System')

        # First Image
        img1 = Image.open(
            r'C:\Users\91999\OneDrive\Desktop\Data '
            r'Science\Face-Recogenization-System\college_images\BestFacialRecognition.jpg')
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=450, height=130)

        # Second Image
        img2 = Image.open(
            r'C:\Users\91999\OneDrive\Desktop\Data '
            r'Science\Face-Recogenization-System\college_images\facialrecognition.png')
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=450, y=0, width=500, height=130)

        # Third Image
        img3 = Image.open(
            r'college_images\Face-Recognition-Software.png')
        img3 = img3.resize((500, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=935, y=0, width=500, height=130)

        # Background Image
        img_bg = Image.open(
            r'C:\Users\91999\OneDrive\Desktop\Data '
            r'Science\Face-Recogenization-System\college_images\bg.png')
        img_bg = img_bg.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)

        bg_image = Label(self.root, image=self.photoimg_bg)
        bg_image.place(x=0, y=130, width=1530, height=710)

        # Making Title
        title_lbl = Label(bg_image, text='FACE  RECOGNITION  SYSTEM  SOFTWARE  ', font=('times new roman', 27, 'bold'),
                          bg='black', fg='white')
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Student button
        img4 = Image.open(
            r'C:\Users\91999\OneDrive\Desktop\Data '
            r'Science\Face-Recogenization-System\college_images\std1.jpg')
        img4 = img4.resize((200, 200), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_image, command=self.student_details, image=self.photoimg4, cursor='hand2')
        b1.place(x=200, y=90, width=200, height=180)

        b1_1 = Button(bg_image, text="STUDENT DETAILS", command=self.student_details, cursor='hand2', font=('times new '
                                                                                                            'roman', 15,
                                                                                                            'bold'),
                      bg='black', fg='white')
        b1_1.place(x=200, y=270, width=200, height=40)

        # Face Detect button
        img5 = Image.open(
            r'C:\Users\91999\OneDrive\Desktop\Data '
            r'Science\Face-Recogenization-System\college_images\face_detector1.jpg')
        img5 = img5.resize((200, 200), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_image, command=self.face_data, image=self.photoimg5, cursor='hand2')
        b2.place(x=450, y=90, width=200, height=180)

        b2_2 = Button(bg_image, text="FACE DETECTOR", command=self.face_data, cursor='hand2', font=('times new roman', 15,
                                                                                          'bold'),
                      bg='black', fg='white')
        b2_2.place(x=450, y=270, width=200, height=40)

        # Attendance button
        img6 = Image.open(
            r'C:\Users\91999\OneDrive\Desktop\Data '
            r'Science\Face-Recogenization-System\college_images\att.jpg')
        img6 = img6.resize((210, 190), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_image, command=self.attendance_data, image=self.photoimg6, cursor='hand2')
        b3.place(x=700, y=90, width=200, height=180)

        b3_3 = Button(bg_image, text="ATTENDANCE", command=self.attendance_data, cursor='hand2', font=('times new '
                                                                                                       'roman', 15, 'bold'),
                      bg='black', fg='white')
        b3_3.place(x=700, y=270, width=200, height=40)

        # Chatbot button
        img7 = Image.open(r'college_images\chat.jpg')
        img7 = img7.resize((210, 190), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b4 = Button(bg_image, command=self.chat_tab, image=self.photoimg7, cursor='hand2')
        b4.place(x=950, y=90, width=200, height=180)

        b4_4 = Button(bg_image, command=self.chat_tab, text="CHATBOT", cursor='hand2', font=('times new roman', 15, 'bold'),
                      bg='black', fg='white')
        b4_4.place(x=950, y=270, width=200, height=40)

        # Train Data button
        img8 = Image.open(
            r'C:\Users\91999\OneDrive\Desktop\Data '
            r'Science\Face-Recogenization-System\college_images\det1.jpg')
        img8 = img8.resize((200, 180), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(bg_image, command=self.train_details, image=self.photoimg8, cursor='hand2')
        b5.place(x=200, y=340, width=200, height=180)

        b5_5 = Button(bg_image,  command=self.train_details, text="TRAIN THE DATA", cursor='hand2', font=('times new '
                                                                                                          'roman', 15,
                                                                                                             'bold'),
                      bg='black', fg='white')
        b5_5.place(x=200, y=500, width=200, height=40)

        # Photos button
        img9 = Image.open(
            r'C:\Users\91999\OneDrive\Desktop\Data '
            r'Science\Face-Recogenization-System\college_images\cam.jpg')
        img9 = img9.resize((200, 200), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6 = Button(bg_image, command=self.open_img, image=self.photoimg9, cursor='hand2')
        b6.place(x=450, y=340, width=200, height=180)

        b6_6 = Button(bg_image, command=self.open_img, text="PHOTOS", cursor='hand2', font=('times new roman', 15,
                                                                                            'bold'),
                      bg='black', fg='white')
        b6_6.place(x=450, y=500, width=200, height=40)

        # Developer button
        img10 = Image.open(
            r'C:\Users\91999\OneDrive\Desktop\Data '
            r'Science\Face-Recogenization-System\college_images\fernando-hernandez-JdoofvUDUwc-unsplash.jpg')
        img10 = img10.resize((300, 300), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b7 = Button(bg_image, command=self.developer_tab, image=self.photoimg10, cursor='hand2')
        b7.place(x=700, y=340, width=200, height=180)

        b7_7 = Button(bg_image, text="DEVELOPER", command=self.developer_tab, cursor='hand2', font=('times new roman', 15, 'bold'),
                      bg='black', fg='white')
        b7_7.place(x=700, y=500, width=200, height=40)

        # Exit button
        img11 = Image.open(
            r'C:\Users\91999\OneDrive\Desktop\Data '
            r'Science\Face-Recogenization-System\college_images\exi.jpg')
        img11 = img11.resize((200, 180), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b8 = Button(bg_image, command=self.exit, image=self.photoimg11, cursor='hand2')
        b8.place(x=950, y=340, width=200, height=180)

        b8_8 = Button(bg_image, text="EXIT", command=self.exit, cursor='hand2', font=('times new roman', 15, 'bold'),
                      bg='black', fg='white')
        b8_8.place(x=950, y=500, width=200, height=40)

    # =============Time=======================================
        def time():
            String = strftime("%H:%M:%S %p")
            lbl.config(text=String)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=('times new roman', 20, 'bold'), bg='black', fg='yellow')
        lbl.place(x=0, y=0, width=220, height=50)
        time()

    # =========Function For Linking Student detail page=======

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def open_img(self):
        os.startfile("Data")

    def train_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendances(self.new_window)

    def exit(self):
        choice = messagebox.askyesno("Exit", "Are you sure to Exit ? ", parent=self.root)
        if choice > 0:
            self.root.destroy()
        else:
            return

    def developer_tab(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def chat_tab(self):
        self.new_window = Toplevel(self.root)
        self.app = ChatBot(self.new_window)


if __name__ == '__main__':
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
