# Student-Database-Managment

This Python script manages a SQLite database for storing student information. It allows you to create a database, define a table structure for storing student data, insert new student records, and retrieve existing records.

## Requirements
- Python 3.x
- SQLite3

## Installation
1. Clone or download the repository.
2. Ensure you have Python installed on your system.
3. No additional installation steps are required for SQLite3, as it is included in Python's standard library.

## Usage
1. Run the script `student_database_management.py`.
2. The script will create a SQLite database named "student_db" if it does not already exist.
3. It defines a table named "students" with columns for student ID, name, and grade.
4. Sample student data is inserted into the table.
5. The script then retrieves and prints the contents of the "students" table.

## Script Structure
- `student_database_management.py`: The main Python script containing the database management functionality.
- `student_db`: SQLite database file where student information is stored.
