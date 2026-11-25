# Employee Task Tracking System

A command-line employee and task management application written in Python. It
uses MySQL to store employee records, tasks, assignments, and comments.

## Features

- Admin login and first-admin registration
- Add, view, search, update, and delete employee records
- Add, view, search, update, and delete tasks
- Assign tasks to employees
- Let employees view assigned tasks, update task status, and add comments
- View task assignments, comments, employee profiles, and completed tasks

## Project explanation

This project is a text-based application: users interact with it by choosing
numbered options in the terminal. The program connects to MySQL when it starts,
then keeps showing the main menu until the user chooses **Exit**.

The application has two kinds of users:

- **Admin:** Signs in with a username and password. Admins can add, view, search,
  update, and delete employee and task records. They can also assign tasks to
  employees and view assignments and comments.
- **Employee:** Signs in with an employee ID. Employees can view tasks assigned
  to them, see task details, change a task's status, leave comments, view their
  completed tasks, and view their employee profile.

The database separates the main kinds of information into tables:

- `users` stores admin login accounts.
- `employees` stores employee IDs and profile details.
- `tasks` stores task descriptions, priority, due date, and status.
- `assigned_tasks` connects employees with tasks and records when a task was
  assigned.
- `comments` stores employee comments linked to a task and an employee.

For example, assigning a task creates a row in `assigned_tasks`; it does not
copy the task details into the employee record. When an employee views their
tasks, the program joins the assignment and task tables and filters by that
employee's ID. Changes made through the menus are saved to MySQL with
`commit()`.

## Requirements

- Python 3
- MySQL Server
- The Python package listed in `requirements.txt`

## Setup

1. Create a MySQL database and tables by running the following SQL in MySQL:

   ```sql
   CREATE DATABASE employee_tracking;
   USE employee_tracking;

   CREATE TABLE employees (
       Emp_id INT PRIMARY KEY,
       name VARCHAR(100) NOT NULL,
       role VARCHAR(100) NOT NULL,
       email VARCHAR(255) NOT NULL,
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );

   CREATE TABLE users (
       user_id INT PRIMARY KEY,
       username VARCHAR(100) NOT NULL UNIQUE,
       password VARCHAR(255) NOT NULL,
       user_type VARCHAR(20) NOT NULL,
       emp_id INT NULL
   );

   CREATE TABLE tasks (
       task_id INT PRIMARY KEY,
       title VARCHAR(255) NOT NULL,
       description TEXT NOT NULL,
       priority VARCHAR(20) NOT NULL,
       due_date DATE NOT NULL,
       status VARCHAR(30) NOT NULL,
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );

   CREATE TABLE assigned_tasks (
       assign_id INT AUTO_INCREMENT PRIMARY KEY,
       task_id INT NOT NULL,
       emp_id INT NOT NULL,
       assigned_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
       FOREIGN KEY (task_id) REFERENCES tasks(task_id) ON DELETE CASCADE,
       FOREIGN KEY (emp_id) REFERENCES employees(Emp_id) ON DELETE CASCADE
   );

   CREATE TABLE comments (
       c_id INT PRIMARY KEY,
       task_id INT NOT NULL,
       emp_id INT NOT NULL,
       comment TEXT NOT NULL,
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
       FOREIGN KEY (task_id) REFERENCES tasks(task_id) ON DELETE CASCADE,
       FOREIGN KEY (emp_id) REFERENCES employees(Emp_id) ON DELETE CASCADE
   );
   ```

2. Update the MySQL connection settings near the top of `main.py` to match
   your MySQL server:

   ```python
   con = db.connect(
       host="localhost",
       user="your_mysql_user",
       password="your_mysql_password",
       database="employee_tracking"
   )
   ```

3. Open a terminal in the project folder and install the dependency:

   ```powershell
   py -m pip install -r requirements.txt
   ```

4. Start the application:

   ```powershell
   py main.py
   ```

## First use

Choose **Admin Login** and enter a username and password. If that username is
not already registered, the application offers to create an admin account.
After signing in, use employee management to add employee records. Employees
can then sign in using their employee ID.

## Security note

This is a learning/demo application. It currently stores admin passwords as
plain text and expects database credentials to be configured in `main.py`.
Do not use it with real accounts or publish real credentials in a public
repository. Production use requires secure password hashing and a safer way to
load secrets.
