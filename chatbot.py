from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import cv2
import os


class ChatBot:

    def __init__(self, root):
        self.root = root
        self.root.geometry('750x580+0+0')
        self.root.title('Face Recognition System')
        self.root.bind("<Return>", self.enter_function)

        # Making Frame
        main_frame = Frame(self.root, bd=2, bg='light blue', width=610)
        main_frame.pack()

        img = Image.open(r'college_images\tra1.jpg')
        img = img.resize((200, 70), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        title_lbl = Label(main_frame, bd=3, relief=RAISED, anchor='nw', width=750, image=self.photoimg, text="  CHAT "
                                                                                                             "WITH "
                                                                                                             "ME",
                          font=('times new roman', 20, 'bold'), fg='white', bg='light blue', compound=LEFT)
        title_lbl.pack(side=TOP)

        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=75, height=20, bd=3, relief=RAISED, font=('times new roman', 14),
                         yscrollcommand=self.scroll_y.set, foreground="green")

        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        btn_frame = Frame(self.root, bd=2, bg='white', width=750, height=75)
        btn_frame.pack(side=BOTTOM)

        label = Label(btn_frame, text="Type Something: ", font=("times new roman", 14), fg='black', bg='light blue')
        label.grid(row=0, column=0, padx=0, pady=0, sticky=W)

        self.entry = StringVar()
        self.entry_fld = ttk.Entry(btn_frame, textvariable=self.entry, width=35, font=('times new roman', 14))
        self.entry_fld.grid(row=0, column=1, padx=5, sticky=W)

        self.send = Button(btn_frame, text="SEND>>", command=self.send, font=("times new roman", 12, "bold"),
                          bg='light blue',
                          fg='black',
                          width=13)
        self.send.grid(row=0, column=2, pady=0, sticky=W)

        self.clear = Button(btn_frame, text="Clear", command=self.clear_data, font=("times new roman", 12, "bold"),
                           bg='light blue',
                           fg='black',
                           width=13)
        self.clear.grid(row=0, column=3, pady=0, sticky=W)

        self.msg = ""
        self.label1 = Label(btn_frame, text=self.msg, font=("times new roman", 14), fg='black', bg='white')
        self.label1.grid(row=2, column=1, padx=5, sticky=W)

    # ==============Function=====================
    def enter_function(self, event):
        self.send.invoke()
        self.entry.set("")

    def clear_data(self):
        self.text.delete("1.0", END)
        self.entry.set("")

    def send(self):

        send = "\t\t\t\t\t\t"+"You : "+self.entry.get()
        self.text.insert(END, "\n"+send)
        self.text.yview(END)
        self.text.focus_set()

        if self.entry.get() == "":
            self.msg = "<<<<<<<  Please enter some input for chat >>>>>>>>"
            self.label1.config(text=self.msg, fg='red')
        else:
            self.msg = ""
            self.label1.config(text=self.msg, fg='red')

        if self.entry.get() == "hello":
            self.text.insert(END, "\n\n"+"Bot : Hi"
                             "\n***************************************************************************")
        elif self.entry.get() == "info":
            self.text.insert(END, "\n*************************** Supported Questions *****************************"
                                  "\n1. what "
                                  "is your name ?"
                                  "\n2. how are you ?\n3. who created you ?\n4. can you speak other language"
                                  " than english ?\n5. how does face recognition work ?\n6. how does face recognition "
                                  "work step by step ?\n7. what is machine learning ?\n8. what is chatbot ?\n9. bye"
                                  "\n10.i am fine "
                                  "\n***************************************************************************")
        elif self.entry.get() == "hi":
            self.text.insert(END, "\n\n" + "Bot : Hello"
                             "\n***************************************************************************")
        elif self.entry.get() == "what is your name ?":
            self.text.insert(END, "\n\n" + "Bot : My name is Mr.Hacker"
                             "\n***************************************************************************")
        elif self.entry.get() == "how are you ?":
            self.text.insert(END, "\n\n" + "Bot : Fine and you"
                             "\n***************************************************************************")
        elif self.entry.get() == "i am fine":
            self.text.insert(END, "\n\n" + "Bot : Great to hear that"
                             "\n***************************************************************************")
        elif self.entry.get() == "who created you ?":
            self.text.insert(END, "\n\n" + "Bot : Aayush Upadhyay created me using tkinter"
                             "\n***************************************************************************")
        elif self.entry.get() == "bye":
            self.text.insert(END, "\n\n" + "Bot : Thank you for chatting"
                             "\n***************************************************************************")
        elif self.entry.get() == "can you speak other language than english ?":
            self.text.insert(END, "\n\n" + "Bot : I am still learning...."
                             "\n***************************************************************************")
        elif self.entry.get() == "how does face recognition work ?":
            self.text.insert(END, "\n\n" + "Bot : It works by identifying and measuring facial features in an "
                                           "image.\n Facial recognition can identify human faces in images or videos,"
                                           "\n determine if the face in two images belongs to the same person, "
                                           "or\n search for a face among a large collection of existing images."
                             "\n***************************************************************************")
        elif self.entry.get() == "how does face recognition work step by step ?":
            self.text.insert(END, "\n\n" + "Bot : step-1 : Face detection >> The camera detects and locates the "
                                           "image"
                                           "\nof the a face either alone or in a crowd...\nStep-2 : Face analysis >>"
                                           " Next,an image of the face is captured and analyzed...\nstep-3 : "
                                           "Converting the image to data using training the image data using openCv"
                                           "\nstep-4 : Finding a match "
                             "\n***************************************************************************")
        elif self.entry.get() == "what is machine learning ?":
            self.text.insert(END, "\n\n" + "Bot : Machine learning is a branch of artificial intelligence (AI) and \n"
                                           "computer science which focuses on the use of data and algorithms\nto "
                                           "imitate the way that humans learn,\ngradually improving its "
                                           "accuracy.Machine learning\nalgorithms are typically created using "
                                           "frameworks that accelerate\nsolution development, such as TensorFlow and "
                                           "PyTorch."
                             "\n***************************************************************************")
        elif self.entry.get() == "what is chatbot ?":
            self.text.insert(END, "\n\n" + "Bot : A chatbot is a conversational application that aids in customer\n "
                                           "service, engagement, and support by replacing or augmenting human "
                                           "\nsupport agents with artificial intelligence (AI) \nand other automation "
                                           "technologies that can communicate\nwith end-users via chat."
                             "\n***************************************************************************")
        else:
            self.text.insert(END, "\n\n" + "Bot : Sorry i didn't get your question"
                             "\n***************************************************************************")


if __name__ == '__main__':
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()
