import streamlit as st
import sqlite3
import pandas as pd

# Connect to SQLite Database
def create_connection():
    conn = sqlite3.connect('job_tracker.db')
    return conn

# Create Table to Store Job Applications
def create_table():
    conn = create_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS job_applications
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  company TEXT,
                  position TEXT,
                  location TEXT,
                  date_applied TEXT,
                  status TEXT,
                  job_description TEXT)''')
    conn.commit()
    conn.close()

# Insert Data into Table
def add_application(company, position, location, date_applied, status, job_description):
    conn = create_connection()
    c = conn.cursor()
    c.execute('''INSERT INTO job_applications
                 (company, position, location, date_applied, status, job_description)
                 VALUES (?, ?, ?, ?, ?, ?)''',
                 (company, position, location, date_applied, status, job_description))
    conn.commit()
    conn.close()

# View All Applications
def view_applications():
    conn = create_connection()
    df = pd.read_sql_query('SELECT * FROM job_applications', conn)
    conn.close()
    return df

# Create Database Table
create_table()

# Streamlit App Layout
st.title("📚 Job Application Tracker")

# Add Job Application Form
with st.form("job_form"):
    st.subheader("Add New Job Application")
    
    company = st.text_input("Company Name")
    position = st.text_input("Position")
    location = st.text_input("Location")
    date_applied = st.date_input("Date Applied")
    status = st.selectbox("Application Status", ["Applied", "Interview Scheduled", "Offer Received", "Rejected", "In Progress"])
    job_description = st.text_area("Job Description/Notes")

    submit_button = st.form_submit_button("Add Application")

# Insert Data if Form is Submitted
if submit_button:
    add_application(company, position, location, date_applied, status, job_description)
    st.success(f"✅ Application for **{position}** at **{company}** added successfully!")

# Display All Applications
st.subheader("📊 View All Applications")
applications_df = view_applications()

if not applications_df.empty:
    st.dataframe(applications_df)
else:
    st.write("No applications added yet. Add your first application!")
