import sqlite3

def create_tables():
    conn = sqlite3.connect('healthcare.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        gender TEXT NOT NULL,
                        contact_details TEXT NOT NULL,
                        medical_history TEXT,
                        surgical_history TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS appointments (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        patient_id INTEGER NOT NULL,
                        provider_id INTEGER NOT NULL,
                        appointment_date TEXT NOT NULL,
                        appointment_time TEXT NOT NULL,
                        status TEXT DEFAULT 'Scheduled',
                        FOREIGN KEY(patient_id) REFERENCES patients(id),
                        FOREIGN KEY(provider_id) REFERENCES users(id))''')

    conn.commit()
    conn.close()

create_tables()
