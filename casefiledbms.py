import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import sqlite3
from datetime import datetime
from PIL import Image, ImageTk

# Connect to SQLite database (or create if not exists)
conn = sqlite3.connect('lawyer_management.db')
c = conn.cursor()

# Create clients table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS clients (
             client_id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT,
             gender TEXT,
             age INTEGER,
             address TEXT,
             case_type TEXT,
             phone TEXT,
             first_meeting_date TEXT,
             next_hearing_date TEXT,
             date_of_judgment TEXT,
             case_status TEXT,
             lawyer_assigned TEXT
             )''')
conn.commit()

class LawyerManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lawyer's Client Management System")
        
        # Load background image using PIL and resize to window dimensions
        try:
            self.bg_image = Image.open('green.jpg')
            self.bg_image = self.bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
            self.bg_label = tk.Label(root, image=self.bg_photo)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except FileNotFoundError:
            messagebox.showerror("Error", "Background image 'background.jpg' not found.")
            root.destroy()
            return
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load background image: {e}")
            root.destroy()
            return

        # Creating labels
        label_name = ttk.Label(root, text="Name:")
        label_name.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        label_gender = ttk.Label(root, text="Gender:")
        label_gender.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        label_age = ttk.Label(root, text="Age:")
        label_age.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        label_address = ttk.Label(root, text="Address:")
        label_address.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

        label_case_type = ttk.Label(root, text="Case Type:")
        label_case_type.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

        label_phone = ttk.Label(root, text="Phone Number:")
        label_phone.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)

        label_first_meeting = ttk.Label(root, text="First Meeting Date:")
        label_first_meeting.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)

        label_next_hearing = ttk.Label(root, text="Next Hearing Date:")
        label_next_hearing.grid(row=7, column=0, padx=10, pady=10, sticky=tk.W)

        label_judgment_date = ttk.Label(root, text="Date of Judgment:")
        label_judgment_date.grid(row=8, column=0, padx=10, pady=10, sticky=tk.W)

        label_status = ttk.Label(root, text="Case Status:")
        label_status.grid(row=9, column=0, padx=10, pady=10, sticky=tk.W)

        label_lawyer = ttk.Label(root, text="Lawyer Assigned:")
        label_lawyer.grid(row=10, column=0, padx=10, pady=10, sticky=tk.W)

        # Creating entry fields and dropdown
        self.entry_name = ttk.Entry(root, width=30)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        self.gender_var = tk.StringVar()
        self.gender_var.set("M")  # default value
        self.gender_dropdown = ttk.Combobox(root, width=27, textvariable=self.gender_var, state='readonly')
        self.gender_dropdown['values'] = ('M', 'F', 'Other')
        self.gender_dropdown.grid(row=1, column=1, padx=10, pady=10)

        self.entry_age = ttk.Entry(root, width=30)
        self.entry_age.grid(row=2, column=1, padx=10, pady=10)

        self.entry_address = ttk.Entry(root, width=30)
        self.entry_address.grid(row=3, column=1, padx=10, pady=10)

        self.case_type_var = tk.StringVar()
        self.case_type_var.set("Criminal")  # default value
        self.case_type_dropdown = ttk.Combobox(root, width=27, textvariable=self.case_type_var, state='readonly')
        self.case_type_dropdown['values'] = ('Criminal', 'Civil', 'Writ')
        self.case_type_dropdown.grid(row=4, column=1, padx=10, pady=10)

        self.entry_phone = ttk.Entry(root, width=30)
        self.entry_phone.grid(row=5, column=1, padx=10, pady=10)

        self.entry_first_meeting = ttk.Entry(root, width=30)
        self.entry_first_meeting.insert(0, datetime.today().strftime('%Y-%m-%d'))
        self.entry_first_meeting.grid(row=6, column=1, padx=10, pady=10)

        self.entry_next_hearing = ttk.Entry(root, width=30)
        self.entry_next_hearing.grid(row=7, column=1, padx=10, pady=10)

        self.entry_judgment_date = ttk.Entry(root, width=30)
        self.entry_judgment_date.grid(row=8, column=1, padx=10, pady=10)

        self.case_status_var = tk.StringVar()
        self.case_status_var.set("Pending")  # default value
        self.case_status_dropdown = ttk.Combobox(root, width=27, textvariable=self.case_status_var, state='readonly')
        self.case_status_dropdown['values'] = ('Pending', 'Closed', 'Ongoing')
        self.case_status_dropdown.grid(row=9, column=1, padx=10, pady=10)

        self.entry_lawyer = ttk.Entry(root, width=30)
        self.entry_lawyer.grid(row=10, column=1, padx=10, pady=10)

        # Buttons
        self.submit_button = ttk.Button(root, text="Submit", width=20, command=self.submit_data)
        self.submit_button.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=50)

        self.clear_button = ttk.Button(root, text="Clear", width=20, command=self.clear_fields)
        self.clear_button.grid(row=12, column=0, columnspan=2, padx=10, pady=10, ipadx=50)

    def clear_fields(self):
        self.entry_name.delete(0, tk.END)
        self.gender_var.set("M")
        self.entry_age.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)
        self.case_type_var.set("Criminal")
        self.entry_phone.delete(0, tk.END)
        self.entry_first_meeting.delete(0, tk.END)
        self.entry_first_meeting.insert(0, datetime.today().strftime('%Y-%m-%d'))
        self.entry_next_hearing.delete(0, tk.END)
        self.entry_judgment_date.delete(0, tk.END)
        self.case_status_var.set("Pending")
        self.entry_lawyer.delete(0, tk.END)

    def submit_data(self):
        name = self.entry_name.get().strip()
        gender = self.gender_var.get()
        age = self.entry_age.get().strip()
        address = self.entry_address.get().strip()
        case_type = self.case_type_var.get()
        phone = self.entry_phone.get().strip()
        first_meeting_date = self.entry_first_meeting.get().strip()
        next_hearing_date = self.entry_next_hearing.get().strip()
        judgment_date = self.entry_judgment_date.get().strip()
        case_status = self.case_status_var.get()
        lawyer_assigned = self.entry_lawyer.get().strip()

        if not (name and age and address and phone and first_meeting_date):
            messagebox.showerror("Error", "Please fill in all required fields.")
            return

        try:
            c.execute('''INSERT INTO clients (name, gender, age, address, case_type, phone, first_meeting_date, next_hearing_date, date_of_judgment, case_status, lawyer_assigned)
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                      (name, gender, int(age), address, case_type, phone, first_meeting_date, next_hearing_date, judgment_date, case_status, lawyer_assigned))
            conn.commit()
            messagebox.showinfo("Success", "Client data added successfully.")
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", f"Error in adding client data: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LawyerManagementApp(root)
    root.mainloop()

# Close the database connection when the application exits
conn.close()
