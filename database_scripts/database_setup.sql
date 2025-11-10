-- Student Management System - Database Setup Script - Hakim Touri 101271029

-- This script creates the database schema and populates initial data
-- for the Student Management System application.

-- Drop the table if it exists
DROP TABLE IF EXISTS students;

-- Create the students table with the specified schema
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,           -- Auto-incrementing primary key
    first_name TEXT NOT NULL,                -- Student's first name 
    last_name TEXT NOT NULL,                 -- Student's last name 
    email TEXT NOT NULL UNIQUE,              -- Student's email (unique)
    enrollment_date DATE                     -- Date when student enrolled
);

-- Add a comment to the table for documentation
COMMENT ON TABLE students IS 'Stores student information including personal details and enrollment date';

-- Add comments to columns for better documentation
COMMENT ON COLUMN students.student_id IS 'Unique identifier for each student (auto-generated)';
COMMENT ON COLUMN students.first_name IS 'Student first name';
COMMENT ON COLUMN students.last_name IS 'Student last name';
COMMENT ON COLUMN students.email IS 'Student email address (must be unique)';
COMMENT ON COLUMN students.enrollment_date IS 'Date when the student enrolled';

-- Insert initial data into the students table
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

-- Display confirmation message and show initial data
SELECT 'Database setup completed successfully!' AS status;

-- Display all records to verify the data was inserted correctly
SELECT * FROM students ORDER BY student_id;