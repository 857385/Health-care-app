import sqlite3
from tkinter import *
from tkinter import messagebox

def add_patient(name, age, gender, contact_details, medical_history, surgical_history):
    conn = sqlite3.connect('healthcare.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO patients (name, age, gender, contact_details, medical_history, surgical_history)
                      VALUES (?, ?, ?, ?, ?, ?)''',
                   (name, age, gender, contact_details, medical_history, surgical_history))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Patient added successfully!")

def view_patients():
    conn = sqlite3.connect('healthcare.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM patients')
    rows = cursor.fetchall()
    conn.close()
    return rows

def edit_patient(patient_id, name, age, gender, contact_details, medical_history, surgical_history):
    conn = sqlite3.connect('healthcare.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE patients SET name = ?, age = ?, gender = ?, contact_details = ?, medical_history = ?, surgical_history = ?
                      WHERE id = ?''',(name, age, gender
, contact_details, medical_history, surgical_history, patient_id))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Patient details updated successfully!")

def delete_patient(patient_id):
    conn = sqlite3.connect('healthcare.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM patients WHERE id = ?', (patient_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Patient deleted successfully!")
