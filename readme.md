Hakim Touri
101271029
COMP3005 - A3 Q1
9 November 2025

Video Demonstration:
https://youtu.be/DA9zoIySJZE

Student Management System
A Python application that connects to a PostgreSQL database to perform CRUD (Create, Read, Update, Delete) operations on student records.

Project Overview
This application provides a command-line interface for managing student records in a PostgreSQL database.

Features
View All Students: Display all student records in a formatted table
Add Student: Insert new student records with validation
Update Email: Modify student email addresses
Delete Student: Remove student records with confirmation

Prerequisites
Before running this application, ensure you have the following installed:

PostgreSQL (version 12 or higher)
Download from: https://www.postgresql.org/download/
Python (version 3.7 or higher)
Download from: https://www.python.org/downloads/
pgAdmin (Usually included with PostgreSQL installation)

Setup Instructions
Step 1: Clone the Repository
bash
git clone https://github.com/hakimtouri/comp3005a3q1.git
cd 3005A3

Step 2: Set Up the Database
Open pgAdmin or use psql command line

Create a new database named student_db:

sql
CREATE DATABASE student_db;

Connect to the database and run the setup script:
Using pgAdmin:

Right-click on student_db → Query Tool
Open database_scripts/database_setup.sql
Click Execute (or F5)


Step 3: Install Python Dependencies
in a bash terminal, paste the following:

# Create a virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

Step 4: Configure Database Connection
Edit student_manager.py and update the connection parameters (around line 200):

python
HOST = "localhost"
DATABASE = "student_db"
USER = "postgres"
PASSWORD = "your_password"  # For TA: Change this to the password of your choice in order to connect.
PORT = "5432"

Running the Application:
Ensure your virtual environment is activated

In a bash terminal, paste the following:
python student_manager.py

Follow the on-screen menu to perform operations:
Enter 1 to view all students
Enter 2 to add a new student
Enter 3 to update a student's email
Enter 4 to delete a student
Enter 5 to exit

Function Descriptions:

1. getAllStudents()
Retrieves and displays all student records from the database in a formatted table.


2. addStudent(first_name, last_name, email, enrollment_date)
Inserts a new student record into the database.
Parameters:
first_name: Student's first name (required)
last_name: Student's last name (required)
email: Student's email address (required, must be unique)
enrollment_date: Enrollment date in YYYY-MM-DD format (required)

Example (python):
db.addStudent("Alice", "Johnson", "alice.j@example.com", "2024-01-15")


3. updateStudentEmail(student_id, new_email)
Updates the email address for a specific student.
Parameters:
student_id: ID of the student to update (required)
new_email: New email address (required)
Example (python):

db.updateStudentEmail(1, "john.newemail@example.com")


4. deleteStudent(student_id)
Deletes a student record from the database.

Parameters:
student_id: ID of the student to delete (required)
Example (python):

db.deleteStudent(3)


Video Demonstration:
https://youtu.be/DA9zoIySJZE