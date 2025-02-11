# Student Result Management System

## Overview

The Student Result Management System is a Python-based application that utilizes Tkinter for the GUI and MySQL for database management. It allows administrators to manage student records efficiently, including adding, updating, deleting, and viewing student results.

## Features

- Add new student records
- Update existing records
- Delete student records
- View all student results in a tabular format
- Search functionality to find specific student records

## Tech Stack

- **Programming Language:** Python
- **GUI Framework:** Tkinter
- **Database:** MySQL
- **Libraries:** 
  - `mysql-connector-python` for database connectivity
  - `Pillow` for image handling

Installation
Clone the Repository:

git clone https://github.com/Shubham1io/SRMs.git
cd SRMs

Install Dependencies:

pip install -r requirements.txt

Set Up the Database:

Create a MySQL database named student_management.
Import the provided database.sql file to set up the necessary tables.

Configure Database Connection:

Update the database connection details in the application to match your MySQL credentials.

Run the Application:

python main.py

Usage

Add Student: Navigate to the 'Add Student' section to input new student details.
Update Student: Select a student record and modify the details as needed.
Delete Student: Remove a student record from the database.
View Results: View all student results in a structured table.

Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.
