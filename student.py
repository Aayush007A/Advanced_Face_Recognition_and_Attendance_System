from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from time import strftime


class Student:

    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Face Recognition System')

        # ==========Variables=============
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_stdid = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_sem = StringVar()
        self.var_name = StringVar()

        # First Image
        img1 = Image.open(
            r'C:\Users\91999\OneDrive\Desktop\Data '
            r'Science\Face-Recogenization-System\college_images\BestFacialRecognition.jpg')
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=450, height=115)

        # Second Image
        img2 = Image.open(
            r'C:\Users\91999\OneDrive\Desktop\Data '
            r'Science\Face-Recogenization-System\college_images\facialrecognition.png')
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=450, y=0, width=500, height=115)

        # Third Image
        img3 = Image.open(
            r'C:\Users\91999\OneDrive\Desktop\Data Science\Face-Recogenization-System\college_images\images.jpg')
        img3 = img3.resize((500, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=935, y=0, width=500, height=115)

        # Background Image
        img_bg = Image.open(
            r'C:\Users\91999\OneDrive\Desktop\Data '
            r'Science\Face-Recogenization-System\college_images\160851.jpg')
        img_bg = img_bg.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)

        bg_image = Label(self.root, image=self.photoimg_bg)
        bg_image.place(x=0, y=115, width=1530, height=730)

        # Making Title
        title_lbl = Label(bg_image, text='STUDENT MANAGEMENT  SYSTEM   ', font=('times new roman', 27, 'bold'),
                          bg='black', fg='white')
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # =============Time=======================================
        def time():
            String = strftime("%H:%M:%S %p")
            lbl.config(text=String)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=('times new roman', 20, 'bold'), bg='black', fg='yellow')
        lbl.place(x=0, y=0, width=220, height=50)
        time()

        # Making Frame
        main_frame = Frame(bg_image, bd=2, bg='white')
        main_frame.place(x=5, y=50, width=1350, height=570)

        # Left Label Frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                font=("times new roman", 12, "bold"), fg='red')
        left_frame.place(x=10, y=10, width=660, height=550)

        img_left = Image.open(
            r'C:\Users\91999\OneDrive\Desktop\Data '
            r'Science\Face-Recogenization-System\college_images\AdobeStock_303989091.jpeg')
        img_left = img_left.resize((650, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=645, height=90)

        # Current course information
        cc_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information",
                              font=("times new roman", 12, "bold"), fg='green')
        cc_frame.place(x=5, y=105, width=645, height=95)

        # Making Labels in current course information
        # Department label
        dep_label = Label(cc_frame, text="Department:", font=("times new roman", 12, "bold"), bg='white')
        dep_label.grid(row=0, column=0, padx=10)
        dep_combo = ttk.Combobox(cc_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"), width=20,
                                 state="readonly")
        dep_combo["values"] = ("Select Department", "CSE", "IT", "Civil", "Mechanical", "Pharmacy")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=5)

        # Year label
        year_label = Label(cc_frame, text="Year:", font=("times new roman", 12, "bold"), bg='white')
        year_label.grid(row=1, column=0, padx=10, sticky=W)
        year_combo = ttk.Combobox(cc_frame, textvariable=self.var_year, font=("times new roman", 12, "bold"), width=20,
                                  state="readonly")
        year_combo["values"] = ("Select Year", "2020-2021", "2021-2022", "2022-2023", "2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=5, sticky=W)

        # Course label
        course_label = Label(cc_frame, text="Course:", font=("times new roman", 12, "bold"), bg='white')
        course_label.grid(row=0, column=2, padx=10, sticky=W)
        course_combo = ttk.Combobox(cc_frame, textvariable=self.var_course, font=("times new roman", 12, "bold"),
                                    width=20,
                                    state="readonly")
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=5, sticky=W)

        # Semester label
        sem_label = Label(cc_frame, text="Semester:", font=("times new roman", 12, "bold"), bg='white')
        sem_label.grid(row=1, column=2, padx=10, sticky=W)
        sem_combo = ttk.Combobox(cc_frame, textvariable=self.var_sem, font=("times new roman", 12, "bold"), width=20,
                                 state="readonly")
        sem_combo["values"] = ("Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4", "Semester-5",
                               "Semester-6", "Semester-7", "Semester-8")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=5, sticky=W)

        # Class student information
        cs_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information",
                              font=("times new roman", 12, "bold"), fg='green')
        cs_frame.place(x=5, y=200, width=645, height=320)

        # Student
        studentId_label = Label(cs_frame, text="StudentID:", font=("times new roman", 12, "bold"), bg='white')
        studentId_label.grid(row=0, column=0, padx=10, sticky=W, pady=5)
        studentId_entry = ttk.Entry(cs_frame, textvariable=self.var_stdid, width=20,
                                    font=("times new roman", 12, "bold"))
        studentId_entry.grid(row=0, column=1, padx=10, sticky=W, pady=5)

        # Class Division
        division_label = Label(cs_frame, text="Class Division:", font=("times new roman", 12, "bold"), bg='white')
        division_label.grid(row=1, column=0, padx=10, sticky=W, pady=5)
        division_entry = ttk.Entry(cs_frame, textvariable=self.var_div, width=20, font=("times new roman", 12, "bold"))
        division_entry.grid(row=1, column=1, padx=10, sticky=W, pady=5)

        # Gender
        gender_label = Label(cs_frame, text="Gender:", font=("times new roman", 12, "bold"), bg='white')
        gender_label.grid(row=2, column=0, padx=10, sticky=W, pady=5)
        # gender_entry = ttk.Entry(cs_frame, textvariable=self.var_gender, width=20, font=("times new roman", 12,
        # "bold")) gender_entry.grid(row=2, column=1, padx=10, sticky=W, pady=5)
        gender_combo = ttk.Combobox(cs_frame, textvariable=self.var_gender, font=("times new roman", 12, "bold"),
                                    width=18,
                                    state="readonly")
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Email
        mail_label = Label(cs_frame, text="Email:", font=("times new roman", 12, "bold"), bg='white')
        mail_label.grid(row=3, column=0, padx=10, sticky=W, pady=5)
        mail_entry = ttk.Entry(cs_frame, textvariable=self.var_email, width=20, font=("times new roman", 12, "bold"))
        mail_entry.grid(row=3, column=1, padx=10, sticky=W, pady=5)

        # Address
        address_label = Label(cs_frame, text="Address:", font=("times new roman", 12, "bold"), bg='white')
        address_label.grid(row=4, column=0, padx=10, sticky=W, pady=5)
        address_entry = ttk.Entry(cs_frame, textvariable=self.var_address, width=20,
                                  font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, sticky=W, pady=5)

        # Student Name
        name_label = Label(cs_frame, text="Student Name:", font=("times new roman", 12, "bold"), bg='white')
        name_label.grid(row=0, column=2, padx=10, sticky=W, pady=5)
        name_entry = ttk.Entry(cs_frame, textvariable=self.var_name, width=20, font=("times new roman", 12, "bold"))
        name_entry.grid(row=0, column=3, padx=10, sticky=W, pady=5)

        # Roll No
        roll_label = Label(cs_frame, text="Roll No:", font=("times new roman", 12, "bold"), bg='white')
        roll_label.grid(row=1, column=2, padx=10, sticky=W, pady=5)
        roll_entry = ttk.Entry(cs_frame, textvariable=self.var_roll, width=20, font=("times new roman", 12, "bold"))
        roll_entry.grid(row=1, column=3, padx=10, sticky=W, pady=5)

        # DOB
        dob_label = Label(cs_frame, text="DOB:", font=("times new roman", 12, "bold"), bg='white')
        dob_label.grid(row=2, column=2, padx=10, sticky=W, pady=5)
        dob_entry = ttk.Entry(cs_frame, textvariable=self.var_dob, width=20, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, sticky=W, pady=5)

        # Phone No
        call_label = Label(cs_frame, text="Phone No:", font=("times new roman", 12, "bold"), bg='white')
        call_label.grid(row=3, column=2, padx=10, sticky=W, pady=5)
        call_entry = ttk.Entry(cs_frame, textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold"))
        call_entry.grid(row=3, column=3, padx=10, sticky=W, pady=5)

        # Teacher Name
        tn_label = Label(cs_frame, text="Teacher Name:", font=("times new roman", 12, "bold"), bg='white')
        tn_label.grid(row=4, column=2, padx=10, sticky=W, pady=5)
        tn_entry = ttk.Entry(cs_frame, textvariable=self.var_teacher, width=20, font=("times new roman", 12, "bold"))
        tn_entry.grid(row=4, column=3, padx=10, sticky=W, pady=5)

        # Radio Button
        self.var_radio1 = StringVar()
        rb1 = ttk.Radiobutton(cs_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        rb1.grid(row=6, column=0)

        rb2 = ttk.Radiobutton(cs_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        rb2.grid(row=6, column=1)

        # Buttons Frame
        btn_frame = Frame(cs_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=630, height=45)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, font=("times new roman", 12, "bold"),
                          bg='blue',
                          fg='white',
                          width=16, height=1)
        save_btn.grid(row=0, column=0, pady=5, sticky=W)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, font=("times new roman", 12, "bold"),
                            bg='blue', fg='white',
                            width=17)
        update_btn.grid(row=0, column=1, pady=5, sticky=W)

        exit_btn = Button(title_lbl, text="Exit", command=self.exit, font=("times new roman", 12, "bold"),
                          bg='white', fg='black',
                          width=17)
        exit_btn.place(x=1200, y=0, width=120, height=40)

        del_btn = Button(btn_frame, text="Delete", command=self.delete_data, font=("times new roman", 12, "bold"),
                         bg='blue',
                         fg='white',
                         width=16)
        del_btn.grid(row=0, column=2, pady=5, sticky=W)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, font=("times new roman", 12, "bold"),
                           bg='blue',
                           fg='white',
                           width=16)
        reset_btn.grid(row=0, column=3, pady=5, sticky=W)

        # Other Buttons Frame
        btn1_frame = Frame(cs_frame, bd=2, relief=RIDGE, bg="white")
        btn1_frame.place(x=0, y=250, width=630, height=45)

        take_photo_btn = Button(btn1_frame, command=self.generate_dataset, text="Take Photo Sample",
                                font=("times new roman", 12,
                                      "bold"),
                                bg='blue',
                                fg='white',
                                width=34)
        take_photo_btn.grid(row=1, column=0, pady=5, sticky=W)

        update_photo_btn = Button(btn1_frame,command=self.generate_dataset , text="Update Photo Sample", font=("times new roman", 12, "bold"),
                                  bg='blue',
                                  fg='white',
                                  width=33)
        update_photo_btn.grid(row=1, column=1, pady=5, sticky=W)

        # Right Label Frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                 font=("times new roman", 12, "bold"), fg='red')
        right_frame.place(x=680, y=10, width=660, height=550)

        img_right = Image.open(
            r'C:\Users\91999\OneDrive\Desktop\Data '
            r'Science\Face-Recogenization-System\college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg')
        img_right = img_right.resize((685, 90), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=645, height=90)

        # ======= Search System =======
        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",
                                  font=("times new roman", 12, "bold"), fg='green')
        search_frame.place(x=5, y=105, width=645, height=70)

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 12, "bold"), bg='blue',
                             fg='white')
        search_label.grid(row=0, column=0, padx=10, sticky=W, pady=5)

        self.var_search = StringVar()
        search_combo = ttk.Combobox(search_frame, textvariable=self.var_search, font=("times new roman", 12),
                                    width=18, state="readonly")
        search_combo["values"] = ("Search", "Department", "Course", "Year", "Semester",
                                  "StudentID", "S_Name", "Division", "RollNo",
                                  "Gender", "DOB", "Email", "PhoneNo", "Address",
                                  "TeacherName", "PhotoSample")
        search_combo.current(0)
        search_combo.grid(row=0, column=3, padx=2, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", command=self.search_data, font=("times new roman", 12, "bold"),
                            bg='blue', fg='white',
                            width=10, height=1)
        search_btn.grid(row=0, column=5, pady=5, sticky=W, padx=5)

        self.var_show = StringVar()
        txt_search = ttk.Entry(search_frame, textvariable=self.var_show, width=16, font=("times new roman", 12,
                                                                                          "bold"))
        txt_search.grid(row=0, column=4, padx=5, sticky=W)

        showAll_btn = Button(search_frame, command=self.fetch_data, text="Show All", font=("times new roman", 12,
                             "bold"), bg='blue', fg='white', width=10)
        showAll_btn.grid(row=0, column=6, pady=5, sticky=W, padx=2)

        # ======= Table Frame =======
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=180, width=645, height=340)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("Department", "Course", "Year", "Semester",
                                                                "StudentID", "StudentName", "Division", "RollNo",
                                                                "Gender", "DOB", "Email", "PhoneNo", "Address",
                                                                "TeacherName", "PhotoStatus"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("StudentID", text="StudentID")
        self.student_table.heading("StudentName", text="S_Name")
        self.student_table.heading("Division", text="Division")
        self.student_table.heading("RollNo", text="RollNO")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("PhoneNo", text="PhoneNo")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("TeacherName", text="TeacherName")
        self.student_table.heading("PhotoStatus", text="PhotoSample")
        self.student_table["show"] = "headings"

        self.student_table.column("Department", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Semester", width=100)
        self.student_table.column("StudentID", width=100)
        self.student_table.column("StudentName", width=100)
        self.student_table.column("Division", width=100)
        self.student_table.column("RollNo", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("PhoneNo", width=100)
        self.student_table.column("Address", width=300)
        self.student_table.column("TeacherName", width=100)
        self.student_table.column("PhotoStatus", width=100)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # =========Function Declaration==========
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_year.get() == "Select Year" or self.var_course.get() \
                == "Select Course" or self.var_sem.get() == "Select Semester" or self.var_teacher.get() == " " or \
                self.var_phone.get() == " " or self.var_dob.get() == " " or self.var_roll.get() == " " or \
                self.var_name.get() == " " or self.var_address.get() == " " or self.var_email.get() == " " or \
                self.var_gender.get() == " " or self.var_div.get() == " " or self.var_stdid.get() == " ":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:

                conn = mysql.connector.connect(host="127.0.0.1", username="Ronaldo7", password="a7b7e777",
                                               database="face_recognition_system")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                  (self.var_dep.get(),
                                   self.var_course.get(),
                                   self.var_year.get(),
                                   self.var_sem.get(),
                                   self.var_stdid.get(),
                                   self.var_name.get(),
                                   self.var_div.get(),
                                   self.var_roll.get(),
                                   self.var_gender.get(),
                                   self.var_dob.get(),
                                   self.var_email.get(),
                                   self.var_phone.get(),
                                   self.var_address.get(),
                                   self.var_teacher.get(),
                                   self.var_radio1.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "All the Information are Saved Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)

    # ======= Fetch Data==========
    def fetch_data(self):
        conn = mysql.connector.connect(host="127.0.0.1", username="Ronaldo7", password="a7b7e777",
                                       database="face_recognition_system")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ============= Get Cursor==========
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_stdid.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # ========== Update Function =========
    def update_data(self):
        global conn
        if self.var_dep.get() == "Select Department" or self.var_year.get() == "Select Year" or self.var_course.get() \
                == "Select Course" or self.var_sem.get() == "Select Semester" or self.var_teacher.get() == " " or \
                self.var_phone.get() == " " or self.var_dob.get() == " " or self.var_roll.get() == " " or \
                self.var_name.get() == " " or self.var_address.get() == " " or self.var_email.get() == " " or \
                self.var_gender.get() == " " or self.var_div.get() == " " or self.var_stdid.get() == " ":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student details ? ",
                                             parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="127.0.0.1", username="Ronaldo7", password="a7b7e777",
                                                   database="face_recognition_system")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Department=%s, Course=%s, Year=%s, Semester=%s, "
                                      "S_Name=%s, Division=%s, RolNo=%s, Gender=%s, DOB=%s, Email=%s, "
                                      "PhoneNo=%s, Address=%s, Teacher_Name=%s, PhotoSample=%s where StudentId=%s", (
                                          self.var_dep.get(),
                                          self.var_course.get(),
                                          self.var_year.get(),
                                          self.var_sem.get(),
                                          self.var_name.get(),
                                          self.var_div.get(),
                                          self.var_roll.get(),
                                          self.var_gender.get(),
                                          self.var_dob.get(),
                                          self.var_email.get(),
                                          self.var_phone.get(),
                                          self.var_address.get(),
                                          self.var_teacher.get(),
                                          self.var_radio1.get(),
                                          self.var_stdid.get(),
                                      ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)

    # ==========Delete Data=========
    def delete_data(self):
        global conn
        if self.var_stdid.get() == " ":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this student details ? ",
                                             parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="127.0.0.1", username="Ronaldo7", password="a7b7e777",
                                                   database="face_recognition_system")
                    my_cursor = conn.cursor()
                    sql = "delete from student where StudentId=%s"
                    value = (self.var_stdid.get(),)
                    my_cursor.execute(sql, value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details successfully deleted", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)

    # =============Reset Data==========
    def reset_data(self):

        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_stdid.set(" "),
        self.var_name.set(" "),
        self.var_div.set(" "),
        self.var_roll.set(" "),
        self.var_gender.set("Male"),
        self.var_dob.set(" "),
        self.var_email.set(" "),
        self.var_phone.set(" "),
        self.var_address.set(" "),
        self.var_teacher.set(" "),
        self.var_radio1.set(" ")

    # =========Generate Dataset or Take photo sample============
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_year.get() == "Select Year" or self.var_course.get() \
                == "Select Course" or self.var_sem.get() == "Select Semester" or self.var_teacher.get() == " " or \
                self.var_phone.get() == " " or self.var_dob.get() == " " or self.var_roll.get() == " " or \
                self.var_name.get() == " " or self.var_address.get() == " " or self.var_email.get() == " " or \
                self.var_gender.get() == " " or self.var_div.get() == " " or self.var_stdid.get() == " ":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="127.0.0.1", username="Ronaldo7", password="a7b7e777",
                                               database="face_recognition_system")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student set Department=%s, Course=%s, Year=%s, Semester=%s, "
                                  "S_Name=%s, Division=%s, RolNo=%s, Gender=%s, DOB=%s, Email=%s, "
                                  "PhoneNo=%s, Address=%s, Teacher_Name=%s, PhotoSample=%s where StudentId=%s", (
                                      self.var_dep.get(),
                                      self.var_course.get(),
                                      self.var_year.get(),
                                      self.var_sem.get(),
                                      self.var_name.get(),
                                      self.var_div.get(),
                                      self.var_roll.get(),
                                      self.var_gender.get(),
                                      self.var_dob.get(),
                                      self.var_email.get(),
                                      self.var_phone.get(),
                                      self.var_address.get(),
                                      self.var_teacher.get(),
                                      self.var_radio1.get(),
                                      self.var_stdid.get(),
                                  ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                # ==========Load Predefined Frontal Face Data==========
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, frames = cap.read()
                    if face_cropped(frames) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(frames), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name = f"Data/user.{str(id)}.{str(img_id)}.jpg"
                        cv2.imwrite(file_name, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)
                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating DataSets Completed !!!")
            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)

    # ==============Exit Screen===========
    def exit(self):
        choice = messagebox.askyesno("Exit", "Are you sure to Exit ? ", parent=self.root)
        if choice > 0:
            self.root.destroy()
        else:
            return

    # =============searching data============
    def search_data(self):
        global conn
        if self.var_search.get() == " " or self.var_show.get() == "":
            messagebox.showerror("Error", "Please enter something for search !!!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="127.0.0.1", username="Ronaldo7", password="a7b7e777",
                                               database="face_recognition_system")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student where "+str(self.var_search.get())+" LIKE '%"+str(
                    self.var_show.get())+"%'")
                data = my_cursor.fetchall()
                if len(data) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)


if __name__ == '__main__':
    root = Tk()
    obj = Student(root)
    root.mainloop()
