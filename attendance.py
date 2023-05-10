from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
import cv2
from time import strftime
from datetime import datetime
from tkinter import ttk
import os
import csv
from tkinter import filedialog, messagebox

mydata = []


class Attendances:

    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('STUDENT ATTENDANCE MANAGEMENT PORTAL')

        # ================Variables==================
        self.var_attn_id = StringVar()
        self.var_attn_roll = StringVar()
        self.var_attn_name = StringVar()
        self.var_attn_dep = StringVar()
        self.var_attn_time = StringVar()
        self.var_attn_date = StringVar()
        self.var_attn_attn = StringVar()

        # First Image
        img1 = Image.open(r'college_images\smart-attendance.jpg')
        img1 = img1.resize((750, 150), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=700, height=150)

        # Second Image
        img2 = Image.open(r'college_images\Team-Management-Software-Development.jpg')
        img2 = img2.resize((780, 150), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=700, y=0, width=780, height=150)

        # Making Title
        title_lbl = Label(self.root, text="STUDENT ATTENDANCE MANAGEMENT PORTAL  ", font=('times new roman', 27,
                                                                                          'bold'),
                          bg='black', fg='white')
        title_lbl.place(x=0, y=150, width=1530, height=50)

        # =============Time=======================================
        def time():
            String = strftime("%H:%M:%S %p")
            lbl.config(text=String)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=('times new roman', 20, 'bold'), bg='black', fg='yellow')
        lbl.place(x=0, y=0, width=220, height=50)
        time()
        # Background Image
        img3 = Image.open(r'college_images\un.jpg')
        img3 = img3.resize((1530, 590), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=0, y=200, width=1530, height=590)

        # Making Frame
        main_frame = Frame(f_lbl, bd=2, bg='white')
        main_frame.place(x=5, y=10, width=1350, height=520)

        # Left Label Frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Information",
                                font=("times new roman", 12, "bold"), fg='red')
        left_frame.place(x=10, y=10, width=660, height=500)

        img_left = Image.open(r'college_images\face-recognition.png')
        img_left = img_left.resize((650, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=650, height=130)

        # Attendance Frame
        attendance_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE)
        attendance_frame.place(x=5, y=135, width=645, height=335)

        # AttendanceId
        AttendanceID_label = Label(attendance_frame, text="AttendanceID:", font=("times new roman", 12, "bold"),
                                   bg='white')
        AttendanceID_label.grid(row=0, column=0, padx=10, sticky=W, pady=10)
        AttendanceID_entry = ttk.Entry(attendance_frame, textvariable=self.var_attn_id, width=20,
                                       font=("times new roman", 12,
                                             "bold"))
        AttendanceID_entry.grid(row=0, column=1, padx=10, sticky=W, pady=10)

        # Name
        name_label = Label(attendance_frame, text="Student Name:", font=("times new roman", 12, "bold"), bg='white')
        name_label.grid(row=1, column=0, padx=10, sticky=W, pady=10)
        name_entry = ttk.Entry(attendance_frame, textvariable=self.var_attn_name, width=20,
                               font=("times new roman", 12, "bold"))
        name_entry.grid(row=1, column=1, padx=10, sticky=W, pady=10)

        # Time
        time_label = Label(attendance_frame, text="Attendance Time:", font=("times new roman", 12, "bold"), bg='white')
        time_label.grid(row=2, column=0, padx=10, sticky=W, pady=10)
        time_entry = ttk.Entry(attendance_frame, textvariable=self.var_attn_time, width=20,
                               font=("times new roman", 12, "bold"))
        time_entry.grid(row=2, column=1, padx=10, sticky=W, pady=10)

        # RollNo Status
        roll_label = Label(attendance_frame, text="Roll No:", font=("times new roman", 12, "bold"),
                           bg='white')
        roll_label.grid(row=0, column=3, padx=5, sticky=W, pady=10)
        roll_entry = ttk.Entry(attendance_frame, textvariable=self.var_attn_roll, width=18,
                               font=("times new roman", 12, "bold"))
        roll_entry.grid(row=0, column=4, padx=5, sticky=W, pady=10)

        # Department
        dep_label = Label(attendance_frame, text="Department:", font=("times new roman", 12, "bold"), bg='white')
        dep_label.grid(row=1, column=3, padx=5, sticky=W, pady=10)
        dep_entry = ttk.Entry(attendance_frame, textvariable=self.var_attn_dep, width=18,
                              font=("times new roman", 12, "bold"))
        dep_entry.grid(row=1, column=4, padx=5, sticky=W, pady=10)

        # Date
        date_label = Label(attendance_frame, text="Attendance Date:", font=("times new roman", 12, "bold"), bg='white')
        date_label.grid(row=2, column=3, padx=5, sticky=W, pady=10)
        date_entry = ttk.Entry(attendance_frame, textvariable=self.var_attn_date, width=18,
                               font=("times new roman", 12, "bold"))
        date_entry.grid(row=2, column=4, padx=5, sticky=W, pady=10)

        # Attendance status label
        status_label = Label(attendance_frame, text="Attendance Status:", font=("times new roman", 12, "bold"),
                             bg='white')
        status_label.grid(row=3, column=0, padx=10)
        status_combo = ttk.Combobox(attendance_frame, textvariable=self.var_attn_attn, font=("times new roman", 12,
                                                                                             "bold"), width=18,
                                    state="readonly")
        status_combo["values"] = ("Choose Status", "Yes", "No")
        status_combo.current(0)
        status_combo.grid(row=3, column=1, padx=2, pady=5)

        btn_frame = Frame(attendance_frame, bd=2, relief=RIDGE, bg="black")
        btn_frame.place(x=5, y=280, width=630, height=45)

        import_btn = Button(btn_frame, text="Import csv", command=self.importCsv, font=("times new roman", 12, "bold"),
                            bg='blue',
                            fg='white',
                            width=16, height=1)
        import_btn.grid(row=0, column=0, pady=5, sticky=W)

        export_btn = Button(btn_frame, text="Export csv", command=self.exportCsv, font=("times new roman", 12, "bold"),
                            bg='blue', fg='white',
                            width=17)
        export_btn.grid(row=0, column=1, pady=5, sticky=W)

        updatecsv_btn = Button(btn_frame, text="Update", command=self.update_data, font=("times new roman", 12,
                                                                                          "bold"),
                            bg='blue',
                            fg='white',
                            width=16)
        updatecsv_btn.grid(row=0, column=2, pady=5, sticky=W)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, font=("times new roman", 12, "bold"),
                           bg='blue',
                           fg='white',
                           width=16)
        reset_btn.grid(row=0, column=3, pady=5, sticky=W)

        save_btn = Button(attendance_frame, text="Save", command=self.add_data, font=("times new roman", 13, "bold"),
                          bg='blue',
                          fg='white',
                          width=16)
        save_btn.place(x=7, y=232, width=190, height=40)

        delete_btn = Button(attendance_frame, text="Delete", command=self.delete_data,
                            font=("times new roman", 13, "bold"),
                            bg='blue',
                            fg='white',
                            width=16)
        delete_btn.place(x=200, y=232, width=190, height=40)

        exit_btn = Button(title_lbl, text="Exit", command=self.exit, font=("times new roman", 12, "bold"),
                          bg='white', fg='black',
                          width=17)
        exit_btn.place(x=1200, y=2, width=120, height=40)

        # Right Label Frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details",
                                 font=("times new roman", 12, "bold"), fg='red')
        right_frame.place(x=680, y=10, width=665, height=500)

        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=5, width=645, height=470)

        # Scrolling
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attendance_table = ttk.Treeview(table_frame, columns=("AttendanceId", "RollNo", "Name", "Department",
                                                                   "Time", "Date", "Attendance"),
                                             xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("AttendanceId", text="AttendanceId")
        self.attendance_table.heading("RollNo", text="RollNo")
        self.attendance_table.heading("Name", text="Name")
        self.attendance_table.heading("Department", text="Department")
        self.attendance_table.heading("Time", text="Time")
        self.attendance_table.heading("Date", text="Date")
        self.attendance_table.heading("Attendance", text="Attendance")
        self.attendance_table["show"] = "headings"

        self.attendance_table.column("AttendanceId", width=100)
        self.attendance_table.column("RollNo", width=100)
        self.attendance_table.column("Name", width=200)
        self.attendance_table.column("Department", width=100)
        self.attendance_table.column("Time", width=100)
        self.attendance_table.column("Date", width=100)
        self.attendance_table.column("Attendance", width=100)
        self.attendance_table.pack(fill=BOTH, expand=1)
        self.attendance_table.bind("<ButtonRelease>", self.get_cursor)
        # self.fetch_data()

    # ============Fetch Data================
    def fetchData(self, rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("", END, values=i)
    # def fetch_data(self, rows):
    #     conn = mysql.connector.connect(host="127.0.0.1", username="Ronaldo7", password="a7b7e777",
    #                                    database="face_recognition_system")
    #     mycursor = conn.cursor()
    #     mycursor.execute("select * from attendance")
    #     rows = mycursor.fetchall()
    #
    #     if len(rows)!= 0:
    #         self.attendance_table.delete(*self.attendance_table.get_children())
    #         for i in rows:
    #             self.attendance_table.insert("",END,values=i)
    #         conn.commit()
    #     conn.close()

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(('CSV File', '*csv'),
                                                                                              ('ALL File', '*.*')),
                                         parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No data for export!!", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Export CSV",
                                               filetypes=(('CSV File', '*csv'),
                                                          ('ALL File', '*.*')),
                                               parent=self.root)
            with open(fln, mode='w', newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Export", "Data Exported successfully at " + os.path.basename(fln))
        except Exception as es:
            messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.attendance_table.focus()
        content = self.attendance_table.item(cursor_row)
        data = content["values"]

        self.var_attn_id.set(data[0])
        self.var_attn_roll.set(data[1])
        self.var_attn_name.set(data[2])
        self.var_attn_dep.set(data[3])
        self.var_attn_time.set(data[4])
        self.var_attn_date.set(data[5])
        self.var_attn_attn.set(data[6])

    def reset_data(self):

        self.var_attn_id.set("")
        self.var_attn_roll.set("")
        self.var_attn_name.set("")
        self.var_attn_dep.set("")
        self.var_attn_time.set("")
        self.var_attn_date.set("")
        self.var_attn_attn.set("Choose Status")

    def add_data(self):
        if self.var_attn_id.get() == "" or self.var_attn_roll.get() == "" or \
                self.var_attn_name.get() \
                == "" or self.var_attn_dep.get() == "" or self.var_attn_time.get() == " " or \
                self.var_attn_date.get() == " " or self.var_attn_attn.get() == "Choose Status":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:

                conn = mysql.connector.connect(host="127.0.0.1", username="Ronaldo7", password="a7b7e777",
                                               database="face_recognition_system")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into attendance values(%s,%s,%s,%s,%s,%s,%s)",
                                  (self.var_attn_id.get(),
                                   self.var_attn_roll.get(),
                                   self.var_attn_name.get(),
                                   self.var_attn_dep.get(),
                                   self.var_attn_time.get(),
                                   self.var_attn_date.get(),
                                   self.var_attn_attn.get()))
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
        my_cursor.execute("select * from attendance")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.attendance_table.delete(*self.attendance_table.get_children())
            for i in data:
                self.attendance_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ==========Delete Data=========
    def delete_data(self):
        global conn
        if self.var_attn_id.get() == " ":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this student attendance details ? ",
                                             parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="127.0.0.1", username="Ronaldo7", password="a7b7e777",
                                                   database="face_recognition_system")
                    my_cursor = conn.cursor()
                    sql = "delete from attendance where AttendanceId=%s"
                    value = (self.var_attn_id.get(),)
                    my_cursor.execute(sql, value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student attendance details successfully deleted", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)

    # ========== Update Function =========
    def update_data(self):
        global conn
        if self.var_attn_id.get() == "" or self.var_attn_roll.get() == "" or \
                self.var_attn_name.get() \
                == "" or self.var_attn_dep.get() == "" or self.var_attn_time.get() == " " or \
                self.var_attn_date.get() == " " or self.var_attn_attn.get() == "Choose Status":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student details ? ",
                                             parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="127.0.0.1", username="Ronaldo7", password="a7b7e777",
                                                   database="face_recognition_system")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update attendance set RollNo=%s, Name=%s, Department=%s, "
                                      "Time=%s, Date=%s, Attendance=%s where AttendanceId=%s", (
                                          self.var_attn_roll.get(),
                                          self.var_attn_name.get(),
                                          self.var_attn_dep.get(),
                                          self.var_attn_time.get(),
                                          self.var_attn_date.get(),
                                          self.var_attn_attn.get(),
                                          self.var_attn_id.get(),
                                      ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success", "Student attendance details successfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)

    def exit(self):
        choice = messagebox.askyesno("Exit", "Are you sure to Exit ? ", parent=self.root)
        if choice > 0:
            self.root.destroy()
        else:
            return


if __name__ == '__main__':
    root = Tk()
    obj = Attendances(root)
    root.mainloop()
