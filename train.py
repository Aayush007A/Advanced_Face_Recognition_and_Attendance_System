from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2 as cv
import os
import numpy as np
from time import strftime


class Train:

    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Face Recognition System')

        # Making Title
        title_lbl = Label(self.root, text="DATASET TRAINING CENTER  ", font=('times new roman', 27, 'bold'),
                          bg='black', fg='white')
        title_lbl.place(x=0, y=0, width=1530, height=50)

        # =============Time=======================================
        def time():
            String = strftime("%H:%M:%S %p")
            lbl.config(text=String)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=('times new roman', 20, 'bold'), bg='black', fg='yellow')
        lbl.place(x=0, y=0, width=220, height=50)
        time()

        # Top Photo
        img_top = Image.open(r'college_images\t_bg1.jpg')
        img_top = img_top.resize((1530, 745), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1530, height=745)

        # Train Dataset Button
        train_btn = Button(self.root, command=self.train_classifier, text="TRAIN  DATASETS", font=("times new roman",
                                                                                                  17, "bold"),
                           bg='blue',
                           fg='white',
                           width=16, height=1)
        train_btn.place(x=648, y=500, width=220, height=50)

        exit_btn = Button(title_lbl, text="Exit", command=self.exit, font=("times new roman", 12, "bold"),
                          bg='white', fg='black',
                          width=17)
        exit_btn.place(x=1200, y=0, width=120, height=40)

    # ============Train Function==========

    def train_classifier(self):
        data_dir = ('Data')
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert('L')  # Gray Scale converter
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv.imshow("Training", imageNp)
            cv.waitKey(1) == 13
        ids = np.array(ids)

        # ===========Train the classifier============
        clf = cv.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("Classifier.xml")
        cv.destroyAllWindows()
        messagebox.showinfo("Result", "Training DataSets Completed !!!", parent=self.root)

    def exit(self):
        choice = messagebox.askyesno("Exit", "Are you sure to Exit ? ", parent=self.root)
        if choice > 0:
            self.root.destroy()
        else:
            return




if __name__ == '__main__':
    root = Tk()
    obj = Train(root)
    root.mainloop()
