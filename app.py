from tkinter import *
from tkinter import ttk, messagebox
from patient_management import add_patient, view_patients, edit_patient, delete_patient
from appointment_scheduling import book_appointment, view_appointments
from authentication import register_user, authenticate_user
from diagnostics import calculate_bmi

class HealthCareApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Healthcare Management System")
        self.root.geometry("800x600")
        self.create_login_window()

    def create_login_window(self):
        self.clear_window()
        Label(self.root, text="Username").grid(row=0, column=0)
        self.username_entry = Entry(self.root)
        self.username_entry.grid(row=0, column=1)

        Label(self.root, text="Password").grid(row=1, column=0)
        self.password_entry = Entry(self.root, show="*")
        self.password_entry.grid(row=1, column=1)

        Button(self.root, text="Login", command=self.login).grid(row=2, column=0, columnspan=2)
        Button(self.root, text="Register", command=self.register).grid(row=3, column=0, columnspan=2)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if authenticate_user(username, password):
            self.create_main_window()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        register_user(username, password)
        messagebox.showinfo("Success", "User registered successfully")

    def create_main_window(self):
        self.clear_window()
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=1, fill="both")

        self.create_patient_management_tab()
        self.create_appointment_tab()
        self.create_diagnostics_tab()

    def create_patient_management_tab(self):
        frame = Frame(self.notebook)
        self.notebook.add(frame, text="Patient Management")

        Label(frame, text="Name").grid(row=0, column=0)
        self.patient_name_entry = Entry(frame)
        self.patient_name_entry.grid(row=0, column=1)

        Label(frame, text="Age").grid(row=1, column=0)
        self.patient_age_entry = Entry(frame)
        self.patient_age_entry.grid(row=1, column=1)

        Label(frame, text="Gender").grid(row=2, column=0)
        self.patient_gender_entry = Entry(frame)
        self.patient_gender_entry.grid(row=2, column=1)

        Label(frame, text="Contact Details").grid(row=3, column=0)
        self.patient_contact_entry = Entry(frame)
        self.patient_contact_entry.grid(row=3, column=1)

        Label(frame, text="Medical History").grid(row=4, column=0)
        self.patient_medical_entry = Entry(frame)
        self.patient_medical_entry.grid(row=4, column=1)

        Label(frame, text="Surgical History").grid(row=5, column=0)
        self.patient_surgical_entry = Entry(frame)
        self.patient_surgical_entry.grid(row=5, column=1)

        Button(frame, text="Add Patient", command=self.add_patient).grid(row=6, column=0, columnspan=2)

        self.patient_list = Listbox(frame)
        self.patient_list.grid(row=7, column=0, columnspan=2, sticky="nsew")
        self.patient_list.bind('<<ListboxSelect>>', self.load_patient_details)

        Button(frame, text="Edit Patient", command=self.edit_patient).grid(row=8, column=0)
        Button(frame, text="Delete Patient", command=self.delete_patient).grid(row=8, column=1)

        self.load_patient_list()

    def add_patient(self):
        name = self.patient_name_entry.get()
        age = int(self.patient_age_entry.get())
        gender = self.patient_gender_entry.get()
        contact_details = self.patient_contact_entry.get()
        medical_history = self.patient_medical_entry.get()
        surgical_history = self.patient_surgical_entry.get()

        add_patient(name, age, gender, contact_details, medical_history, surgical_history)
        self.load_patient_list()

    def load_patient_list(self):
        self.patient_list.delete(0, END)
        patients = view_patients()
        for patient in patients:
            self.patient_list.insert(END, patient)

    def load_patient_details(self, event):
        selected_index = self.patient_list.curselection()
        if not selected_index:
            return
        patient = self.patient_list.get(selected_index)
        self.selected_patient_id = patient[0]
        self.patient_name_entry.delete(0, END)
        self.patient_name_entry.insert(0, patient[1])
        self.patient_age_entry.delete(0, END)
        self.patient_age_entry.insert(0, patient[2])
        self.patient_gender_entry.delete(0, END)
        self.patient_gender_entry.insert(0, patient[3])
        self.patient_contact_entry.delete(0, END)
        self.patient_contact_entry.insert(0, patient[4])
        self.patient_medical_entry.delete(0, END)
        self.patient_medical_entry.insert(0, patient[5])
        self.patient_surgical_entry.delete(0, END)
        self.patient_surgical_entry.insert(0, patient[6])

    def edit_patient(self):
        name = self.patient_name_entry.get()
        age = int(self.patient_age_entry.get())
        gender = self.patient_gender_entry.get()
        contact_details = self.patient_contact_entry.get()
        medical_history = self.patient_medical_entry.get()
        surgical_history = self.patient_surgical_entry.get()

        edit_patient(self.selected_patient_id, name, age, gender, contact_details, medical_history, surgical_history)
        self.load_patient_list()

    def delete_patient(self):
        delete_patient(self.selected_patient_id)
        self.load_patient_list()

    def create_appointment_tab(self):
        frame = Frame(self.notebook)
        self.notebook.add(frame, text="Appointment Scheduling")

        Label(frame, text="Patient ID").grid(row=0, column=0)
        self.appointment_patient_id_entry = Entry(frame)
        self.appointment_patient_id_entry.grid(row=0, column=1)

        Label(frame, text="Provider ID").grid(row=1, column=0)
        self.appointment_provider_id_entry = Entry(frame)
        self.appointment_provider_id_entry.grid(row=1, column=1)

        Label(frame, text="Date").grid(row=2, column=0)
        self.appointment_date_entry = Entry(frame)
        self.appointment_date_entry.grid(row=2, column=1)

        Label(frame, text="Time").grid(row=3, column=0)
        self.appointment_time_entry = Entry(frame)
        self.appointment_time_entry.grid(row=3, column=1)

        Button(frame, text="Book Appointment", command=self.book_appointment).grid(row=4, column=0, columnspan=2)

        self.appointment_list = Listbox(frame)
        self.appointment_list.grid(row=5, column=0, columnspan=2, sticky="nsew")

        self.load_appointment_list()

    def book_appointment(self):
        patient_id = int(self.appointment_patient_id_entry.get())
        provider_id = int(self.appointment_provider_id_entry.get())
        appointment_date = self.appointment_date_entry.get()
        appointment_time = self.appointment_time_entry.get()

        book_appointment(patient_id, provider_id, appointment_date, appointment_time)
        self.load_appointment_list()

    def load_appointment_list(self):
        self.appointment_list.delete(0, END)
        appointments = view_appointments()
        for appointment in appointments:
            self.appointment_list.insert(END, appointment)

    def create_diagnostics_tab(self):
        frame = Frame(self.notebook)
        self.notebook.add(frame, text="Diagnostics")

        Label(frame, text="Weight (kg)").grid(row=0, column=0)
        self.weight_entry = Entry(frame)
        self.weight_entry.grid(row=0, column=1)

        Label(frame, text="Height (m)").grid(row=1, column=0)
        self.height_entry = Entry(frame)
        self.height_entry.grid(row=1, column=1)

        Button(frame, text="Calculate BMI", command=self.calculate_bmi).grid(row=2, column=0, columnspan=2)

        self.bmi_result_label = Label(frame, text="")
        self.bmi_result_label.grid(row=3, column=0, columnspan=2)

    def calculate_bmi(self):
        weight = float(self.weight_entry.get())
        height = float(self.height_entry.get())
        bmi = calculate_bmi(weight, height)
        self.bmi_result_label.config(text=f"BMI: {bmi}")

if __name__ == "__main__":
    root = Tk()
    app = HealthCareApp(root)
    root.mainloop()
