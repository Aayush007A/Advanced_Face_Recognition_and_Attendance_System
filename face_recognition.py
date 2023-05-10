from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
import cv2
from time import strftime
from datetime import datetime
from tkinter import messagebox


class Face_Recognition:

    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Face Recognition System')

        # Making Title
        title_lbl = Label(self.root, text=" FACE RECOGNITION CENTER  ", font=('times new roman', 27, 'bold'),
                          bg='black', fg='white')
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Left Photo
        img_top = Image.open(r'college_images\face_detector1.jpg')
        img_top = img_top.resize((650, 745), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=650, height=745)

        # Right Photo
        img_bottom = Image.open(r'college_images'
                                r'\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg')
        img_bottom = img_bottom.resize((900, 720), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=45, width=900, height=700)

        # Identify Button
        train_btn = Button(self.root, text="IDENTIFY YOURSELF", command=self.face_recog, font=("times new roman", 12, "bold"),
                           bg='blue',
                           fg='white',
                           width=20, height=1)
        train_btn.place(x=990, y=670, width=200, height=50)

        exit_btn = Button(title_lbl, text="Exit", command=self.exit, font=("times new roman", 12, "bold"),
                          bg='white', fg='black',
                          width=17)
        exit_btn.place(x=1200, y=0, width=120, height=40)

    # ==============Attendance=================

    def mark_attendance(self, s, j, i, k):
        with open("Attendance.csv", "r+", newline="") as f:
            mydata = f.readlines()
            name_list = []
            for line in mydata:
                entry = line.split((","))
                name_list.append(entry[0])
            if (s not in name_list) and (j not in name_list) and (i not in name_list) and (k not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{s},{j},{i},{k},{dtString},{d1},Present")

    # ==============Face recognition==========

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                ids, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))
                conn = mysql.connector.connect(host="127.0.0.1", username="Ronaldo7", password="a7b7e777",
                                               database="face_recognition_system")
                my_cursor = conn.cursor()

                my_cursor.execute("select S_Name from student where StudentId=" + str(ids))
                i = my_cursor.fetchone()
                i = "+".join(i)

                my_cursor.execute("select RolNo from student where StudentId=" + str(ids))
                j = my_cursor.fetchone()
                j = "+".join(j)

                my_cursor.execute("select Department from student where StudentId=" + str(ids))
                k = my_cursor.fetchone()
                k = "+".join(k)

                my_cursor.execute("select StudentId from student where StudentId=" + str(ids))
                s = my_cursor.fetchone()
                s = "+".join(s)

                if confidence > 77:
                    cv2.putText(img, f"StudentId: {s}", (x, y - 85), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 1)
                    cv2.putText(img, f"RollNo: {j}", (x, y - 60), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 1)
                    cv2.putText(img, f"Name: {i}", (x, y - 35), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 1)
                    cv2.putText(img, f"Department: {k}", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 1)
                    self.mark_attendance(s, j, i, k)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("Classifier.xml")

        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)
            if cv2.waitKey(1) == 13:
                break
        cap.release()
        cv2.destroyAllWindows()

    def exit(self):
        choice = messagebox.askyesno("Exit", "Are you sure to Exit ? ", parent=self.root)
        if choice > 0:
            self.root.destroy()
        else:
            return


if __name__ == '__main__':
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
