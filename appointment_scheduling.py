import sqlite3
from tkinter import *
from tkinter import messagebox

def book_appointment(patient_id, provider_id, appointment_date, appointment_time):
    conn = sqlite3.connect('healthcare.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO appointments (patient_id, provider_id, appointment_date, appointment_time)
                      VALUES (?, ?, ?, ?)''',
                   (patient_id, provider_id, appointment_date, appointment_time))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Appointment booked successfully!")

def view_appointments():
    conn = sqlite3.connect('healthcare.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM appointments')
    rows = cursor.fetchall()
    conn.close()
    return rows
