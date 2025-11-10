"""
Student Management System - PostgreSQL Database Application
This application performs CRUD operations on a PostgreSQL database containing student records.
"""

import psycopg2
from psycopg2 import Error
from datetime import datetime
from typing import Optional, List, Tuple


class StudentDatabase:
    """
    A class to manage database connections and operations for the students table.
    """
    
    def __init__(self, host: str, database: str, user: str, password: str, port: str = "5432"):
        """
        Initialize database connection parameters.
        
        Args:
            host: Database host address
            database: Database name
            user: Database username
            password: Database password
            port: Database port (default: 5432)
        """
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.connection = None
        self.cursor = None
    
    def connect(self) -> bool:
        """
        Establish connection to the PostgreSQL database.
        
        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print("✓ Successfully connected to PostgreSQL database")
            return True
        except Error as e:
            print(f"✗ Error connecting to PostgreSQL database: {e}")
            return False
    
    def disconnect(self):
        """
        Close database connection and cursor.
        """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("✓ Database connection closed")
    
    def getAllStudents(self) -> List[Tuple]:
        """
        Retrieve and display all records from the students table.
        
        Returns:
            List[Tuple]: List of all student records
        """
        try:
            # Execute SELECT query to fetch all students
            query = """
                SELECT student_id, first_name, last_name, email, enrollment_date 
                FROM students 
                ORDER BY student_id
            """
            self.cursor.execute(query)
            students = self.cursor.fetchall()
            
            # Display results in formatted table
            print("\n" + "="*80)
            print("ALL STUDENTS")
            print("="*80)
            print(f"{'ID':<5} {'First Name':<15} {'Last Name':<15} {'Email':<30} {'Enrollment Date':<15}")
            print("-"*80)
            
            if students:
                for student in students:
                    student_id, first_name, last_name, email, enrollment_date = student
                    print(f"{student_id:<5} {first_name:<15} {last_name:<15} {email:<30} {enrollment_date}")
                print(f"\nTotal students: {len(students)}")
            else:
                print("No students found in the database.")
            
            print("="*80 + "\n")
            return students
            
        except Error as e:
            print(f"✗ Error retrieving students: {e}")
            return []
    
    def addStudent(self, first_name: str, last_name: str, email: str, enrollment_date: str) -> bool:
        """
        Insert a new student record into the students table.
        
        Args:
            first_name: Student's first name
            last_name: Student's last name
            email: Student's email address (must be unique)
            enrollment_date: Date of enrollment (format: YYYY-MM-DD)
        
        Returns:
            bool: True if insertion successful, False otherwise
        """
        try:
            # Prepare INSERT query with parameterized values to prevent SQL injection
            query = """
                INSERT INTO students (first_name, last_name, email, enrollment_date) 
                VALUES (%s, %s, %s, %s)
                RETURNING student_id
            """
            
            # Execute query with parameters
            self.cursor.execute(query, (first_name, last_name, email, enrollment_date))
            
            # Get the auto-generated student_id
            student_id = self.cursor.fetchone()[0]
            
            # Commit the transaction
            self.connection.commit()
            
            print(f"✓ Successfully added student: {first_name} {last_name} (ID: {student_id})")
            return True
            
        except Error as e:
            # Rollback transaction on error
            self.connection.rollback()
            print(f"✗ Error adding student: {e}")
            return False
    
    def updateStudentEmail(self, student_id: int, new_email: str) -> bool:
        """
        Update the email address for a student with the specified student_id.
        
        Args:
            student_id: ID of the student to update
            new_email: New email address
        
        Returns:
            bool: True if update successful, False otherwise
        """
        try:
            # First we check if the student exists
            check_query = "SELECT first_name, last_name FROM students WHERE student_id = %s"
            self.cursor.execute(check_query, (student_id,))
            student = self.cursor.fetchone()
            
            if not student:
                print(f"✗ Student with ID {student_id} not found")
                return False
            
            # Prepare UPDATE query
            query = """
                UPDATE students 
                SET email = %s 
                WHERE student_id = %s
            """
            
            # Execute update query
            self.cursor.execute(query, (new_email, student_id))
            
            # Commit the transaction
            self.connection.commit()
            
            print(f"✓ Successfully updated email for {student[0]} {student[1]} (ID: {student_id})")
            print(f"  New email: {new_email}")
            return True
            
        except Error as e:
            # Rollback transaction on error
            self.connection.rollback()
            print(f"✗ Error updating student email: {e}")
            return False
    
    def deleteStudent(self, student_id: int) -> bool:
        """
        Delete the record of the student with the specified student_id.
        
        Args:
            student_id: ID of the student to delete
        
        Returns:
            bool: True if deletion successful, False otherwise
        """
        try:
            # First, check if the student exists and get their info
            check_query = "SELECT first_name, last_name FROM students WHERE student_id = %s"
            self.cursor.execute(check_query, (student_id,))
            student = self.cursor.fetchone()
            
            if not student:
                print(f"✗ Student with ID {student_id} not found")
                return False
            
            # Prepare DELETE query
            query = "DELETE FROM students WHERE student_id = %s"
            
            # Execute delete query
            self.cursor.execute(query, (student_id,))
            
            # Commit the transaction
            self.connection.commit()
            
            print(f"✓ Successfully deleted student: {student[0]} {student[1]} (ID: {student_id})")
            return True
            
        except Error as e:
            # Rollback transaction on error
            self.connection.rollback()
            print(f"✗ Error deleting student: {e}")
            return False


def display_menu():
    """
    Display the interactive menu for the application.
    """
    print("\n" + "="*50)
    print("STUDENT MANAGEMENT SYSTEM")
    print("="*50)
    print("1. View All Students")
    print("2. Add New Student")
    print("3. Update Student Email")
    print("4. Delete Student")
    print("5. Exit")
    print("="*50)


def main():
    """
    Main function to run the Student Management System application.
    """
    print("\n" + "="*50)
    print("Welcome to Student Management System")
    print("="*50)
    
    # Database connection parameters
    HOST = "localhost"
    DATABASE = "student_db"
    USER = "postgres"
    PASSWORD = "mypassword"
    PORT = "5432"
    
    # Create database instance
    db = StudentDatabase(HOST, DATABASE, USER, PASSWORD, PORT)
    
    # Connect to database
    if not db.connect():
        print("Failed to connect to database. Please check your connection parameters.")
        return
    
    # Main application loop
    try:
        while True:
            display_menu()
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == "1":
                # View all students
                db.getAllStudents()
                input("\nPress Enter to continue...")
                
            elif choice == "2":
                # Add new student
                print("\n--- Add New Student ---")
                first_name = input("Enter first name: ").strip()
                last_name = input("Enter last name: ").strip()
                email = input("Enter email: ").strip()
                enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ").strip()
                
                # Validate date format
                try:
                    datetime.strptime(enrollment_date, "%Y-%m-%d")
                    db.addStudent(first_name, last_name, email, enrollment_date)
                except ValueError:
                    print("✗ Invalid date format. Please use YYYY-MM-DD")
                
                input("\nPress Enter to continue...")
                
            elif choice == "3":
                # Update student email
                print("\n--- Update Student Email ---")
                try:
                    student_id = int(input("Enter student ID: ").strip())
                    new_email = input("Enter new email: ").strip()
                    db.updateStudentEmail(student_id, new_email)
                except ValueError:
                    print("✗ Invalid student ID. Please enter a number.")
                
                input("\nPress Enter to continue...")
                
            elif choice == "4":
                # Delete student
                print("\n--- Delete Student ---")
                try:
                    student_id = int(input("Enter student ID to delete: ").strip())
                    confirm = input(f"Are you sure you want to delete student {student_id}? (yes/no): ").strip().lower()
                    if confirm == "yes":
                        db.deleteStudent(student_id)
                    else:
                        print("Deletion cancelled.")
                except ValueError:
                    print("✗ Invalid student ID. Please enter a number.")
                
                input("\nPress Enter to continue...")
                
            elif choice == "5":
                # Exit application
                print("\nThank you for using Student Management System!")
                break
                
            else:
                print("✗ Invalid choice. Please enter a number between 1 and 5.")
                input("\nPress Enter to continue...")
    
    finally:
        # Ensure database connection is closed
        db.disconnect()


if __name__ == "__main__":
    main()