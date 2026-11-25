# Database connection
import mysql.connector as db

con = db.connect(
    host="localhost",
    user="root",
    password="root",
    database="employee_tracking"
)

cur = con.cursor()

# Main menu
while True:

    print("="*10, "Employee Task Tracking system", "="*10)

    print("1.Admin Login")
    print("2.Employee Login")
    print("3. Exit")

    print("="*10, "Employee Task Tracking system", "="*10)

    choice = input("Enter your choice: ")

    # Admin login
    if choice == '1':

        username = input("Enter Admin Username: ")
        password = input("Enter Admin Password: ")

        cur.execute(
            "SELECT * FROM users WHERE username = %s AND password = %s AND user_type = 'Admin'",
            (username, password)
        )

        result = cur.fetchone()

        if result is not None:

            print("Admin Login Successfully")

            # Admin dashboard
            while True:
                print("="*10,"Admin Dashboard","="*10)

                print("1.Employee Management")
                print("2.Task Management")
                print("3.Assign Tasks")
                print("4.View Assigned Tasks")
                print("5.View comments")
                print("6. Logout")

                admin_choice=input("Enter your choice: ")

                if admin_choice=='1':
                    # Employee management
                    while True:
                        print("="*10,"Employee Management","="*10)
                        print('1.Add Employee')
                        print('2.View All Employees')
                        print('3.Search Employee')
                        print('4.Update Employee')
                        print('5.Delete Employee')
                        print('6.Back to Admin Dashboard')

                        emp_choice=input("Enter Your choice: ")

                        if emp_choice=='1':
                            # Add employee
                            emp_id=int(input("Enter Employee ID: "))
                            name=input("Enter Employee Name: ")
                            role=input("Enter Employee Role: ")
                            email=input("Enter Employee Email: ")

                            query=""" Insert into employees(Emp_id,
                                    name,role,email) values(%s,%s,%s,%s)"""

                            cur.execute(query,(emp_id,name,role,email))
                            con.commit()

                            print("Employee Added Succesfully!")


                        elif emp_choice=='2':
                            # View employees
                            query="Select * from employees"
                            cur.execute(query)
                            data=cur.fetchall()
                            for row in data:
                                print(row)

                        elif emp_choice=='3':
                            # Search employee
                            emp_id=int(input("Enter Employee ID to search: "))
                            query="Select * from employees where Emp_id=%s"
                            cur.execute(query,(emp_id,))
                            data=cur.fetchone()
                            for row in data:
                                print(row)



                        elif emp_choice=='4':
                            # Update employee
                            emp_id = int(input("Enter Employee ID to Update: "))

                            # Check whether employee exists
                            query = "SELECT * FROM employees WHERE Emp_id = %s"

                            cur.execute(query, (emp_id,))

                            employee = cur.fetchone()

                            if employee:

                                print("\nEmployee Found")
                                print("\nCurrent Employee Details")

                                print("Employee ID:", employee[0])
                                print("Employee Name:", employee[1])
                                print("Employee Role:", employee[2])
                                print("Employee Email:", employee[3])
                                print("Created At:", employee[4])

                                # Get new employee details
                                print("\nEnter New Employee Details")

                                name = input("Enter New Employee Name: ")
                                role = input("Enter New Employee Role: ")
                                email = input("Enter New Employee Email: ")

                                # Update employee details
                                query = """UPDATE employees
                                        SET name = %s, role = %s, email = %s
                                        WHERE Emp_id = %s"""

                                cur.execute(query, (name, role, email, emp_id))

                                con.commit()

                                print("\nEmployee Updated Successfully")

                            else:
                                print("\nEmployee Not Found")
                                                    
                        elif emp_choice=='5':
                            # Delete employee
                            emp_id=int(input("Enter Employee ID to delete: "))
                            query = "SELECT * FROM employees WHERE Emp_id = %s"
                            
                            cur.execute(query, (emp_id,))
                            
                            employee = cur.fetchone()
                            
                            if employee:
                                print("Employee found")
                                confirm = input("Are you sure you want to delete this employee? (yes/no): ")

                                if confirm.lower() == 'yes':

                                    query = "DELETE FROM employees WHERE Emp_id = %s"

                                    cur.execute(query, (emp_id,))

                                    con.commit()

                                    print("Employee Deleted Successfully")

                                else:
                                    print("Employee Deletion Cancelled")

                            else:
                                print("Employee not found")
                            

                        elif emp_choice=='6':
                            print("Returning to Admin Dashboard")
                            break

                        else:
                            print("Invalid Choice.Try Again!!")


                elif admin_choice=='2':
                    # Task management
                    while True:

                        print("\n========== TASK MANAGEMENT ==========")
                        print("1. Add Task")
                        print("2. View All Tasks")
                        print("3. Search Task")
                        print("4. Update Task")
                        print("5. Delete Task")
                        print("6. Back to Admin Dashboard")

                        task_choice = input("Enter Your Choice: ")

                        # 1. ADD TASK
                        if task_choice == '1':

                            task_id = int(input("Enter Task ID: "))
                            title = input("Enter Task Title: ")
                            description = input("Enter Task Description: ")
                            priority = input("Enter Task Priority: ")
                            due_date = input("Enter Due Date (YYYY-MM-DD): ")
                            status = input("Enter Task Status: ")

                            query = """INSERT INTO tasks
                                    (task_id, title, description, priority, due_date, status)
                                    VALUES (%s, %s, %s, %s, %s, %s)"""

                            cur.execute(query, (task_id, title, description,
                                                priority, due_date, status))

                            con.commit()

                            print("Task Added Successfully")


                        # 2. VIEW ALL TASKS
                        elif task_choice == '2':

                            query = "SELECT * FROM tasks"

                            cur.execute(query)

                            tasks = cur.fetchall()

                            if tasks:

                                print("\n========== ALL TASKS ==========")

                                for task in tasks:

                                    print("\nTask ID:", task[0])
                                    print("Title:", task[1])
                                    print("Description:", task[2])
                                    print("Priority:", task[3])
                                    print("Due Date:", task[4])
                                    print("Status:", task[5])
                                    print("Created At:", task[6])

                            else:
                                print("No Tasks Found")


                        # 3. SEARCH TASK
                        elif task_choice == '3':

                            task_id = int(input("Enter Task ID to Search: "))

                            query = "SELECT * FROM tasks WHERE task_id = %s"

                            cur.execute(query, (task_id,))

                            task = cur.fetchone()

                            if task:

                                print("\n========== TASK DETAILS ==========")

                                print("Task ID:", task[0])
                                print("Title:", task[1])
                                print("Description:", task[2])
                                print("Priority:", task[3])
                                print("Due Date:", task[4])
                                print("Status:", task[5])
                                print("Created At:", task[6])

                            else:
                                print("Task Not Found")


                        # 4. UPDATE TASK
                        elif task_choice == '4':

                            task_id = int(input("Enter Task ID to Update: "))

                            query = "SELECT * FROM tasks WHERE task_id = %s"

                            cur.execute(query, (task_id,))

                            task = cur.fetchone()

                            if task:

                                print("\nCurrent Task Details")

                                print("Task ID:", task[0])
                                print("Title:", task[1])
                                print("Description:", task[2])
                                print("Priority:", task[3])
                                print("Due Date:", task[4])
                                print("Status:", task[5])

                                print("\nEnter New Task Details")

                                title = input("Enter New Task Title: ")
                                description = input("Enter New Description: ")
                                priority = input("Enter New Priority: ")
                                due_date = input("Enter New Due Date (YYYY-MM-DD): ")
                                status = input("Enter New Status: ")

                                query = """UPDATE tasks
                                        SET title = %s,
                                            description = %s,
                                            priority = %s,
                                            due_date = %s,
                                            status = %s
                                        WHERE task_id = %s"""

                                cur.execute(query, (title, description, priority,
                                                    due_date, status, task_id))

                                con.commit()

                                print("Task Updated Successfully")

                            else:
                                print("Task Not Found")


                        # 5. DELETE TASK
                        elif task_choice == '5':

                            task_id = int(input("Enter Task ID to Delete: "))

                            query = "SELECT * FROM tasks WHERE task_id = %s"

                            cur.execute(query, (task_id,))

                            task = cur.fetchone()

                            if task:

                                print("\nTask Found")
                                print("Task ID:", task[0])
                                print("Task Title:", task[1])
                                print("Task Priority:", task[3])

                                confirm = input(
                                    "Are you sure you want to delete this task? (yes/no): "
                                )

                                if confirm.lower() == 'yes':

                                    query = "DELETE FROM tasks WHERE task_id = %s"

                                    cur.execute(query, (task_id,))

                                    con.commit()

                                    print("Task Deleted Successfully")

                                else:
                                    print("Task Deletion Cancelled")

                            else:
                                print("Task Not Found")


                        # 6. BACK TO ADMIN DASHBOARD
                        elif task_choice == '6':

                            print("Returning to Admin Dashboard...")
                            break


                        else:
                            print("Invalid Choice. Please Try Again.")

                elif admin_choice=='3':
                    # Assign task
                    task_id = int(input("Enter Task ID: "))
                    emp_id = int(input("Enter Employee ID: "))

                    query = """
                        INSERT INTO assigned_tasks (task_id, emp_id)
                        VALUES (%s, %s)
                    """

                    cur.execute(query, (task_id, emp_id))
                    con.commit()

                    print("Task assigned successfully!")

                elif admin_choice=='4':
                    # View assigned tasks
                    query = "SELECT * FROM assigned_tasks"

                    cur.execute(query)

                    result = cur.fetchall()

                    if result:
                        print("\n------ ASSIGNED TASKS ------")

                        for row in result:
                            print("Assignment ID:", row[0])
                            print("Task ID:", row[1])
                            print("Employee ID:", row[2])
                            print("Assigned Date:", row[3])
                            print("----------------------------")

                    else:
                        print("No assigned tasks found.")

                elif admin_choice=='5':
                    # View comments
                    query = "SELECT * FROM comments"

                    cur.execute(query)

                    result = cur.fetchall()

                    if result:
                        print("\n------ EMPLOYEE COMMENTS ------")

                        for row in result:
                            print("Comment ID:", row[0])
                            print("Task ID:", row[1])
                            print("Employee ID:", row[2])
                            print("Comment:", row[3])
                            print("Created At:", row[4])
                            print("-------------------------------")

                    else:
                        print("No comments found.")
                elif admin_choice=='6':
                    print("Admin Looged Out")
                    break
                else:
                    print("Invalid Choice.Try Again!!") 
        

        else:

            # Admin registration
            cur.execute(
                "SELECT * FROM users WHERE username = %s",
                (username,)
            )

            existing_user = cur.fetchone()

            if existing_user is not None:

                print("Incorrect Password or Account Type")

            else:

                print("Admin Account Not Found")

                register = input("Do you want to register? (yes/no): ")

                if register.lower() == 'yes':

                    print("----- Admin Registration -----")

                    new_password = input("Create Admin Password: ")

                    cur.execute(
                        "SELECT MAX(user_id) FROM users"
                    )

                    last_id = cur.fetchone()[0]

                    new_id = 1 if last_id is None else last_id + 1

                    cur.execute(
                        "INSERT INTO users (user_id, username, password, user_type, emp_id) VALUES (%s, %s, %s, %s, %s)",
                        (new_id, username, new_password, 'Admin', None)
                    )

                    con.commit()

                    print("Admin Registered Successfully")

                else:

                    print("Registration Cancelled")


    elif choice == '2':

        # Employee login
        emp_id = int(input("Enter Employee ID: "))
        cur.execute(
            "SELECT Emp_id FROM employees WHERE Emp_id = %s",
            (emp_id,)
        )

        if cur.fetchone():

            # Employee dashboard
            while True:

                print("\n========== EMPLOYEE DASHBOARD ==========")
                print("1. View My Assigned Tasks")
                print("2. View Task Details")
                print("3. Update Task Status")
                print("4. Add Comments")
                print("5. View Completed Tasks")
                print("6. View My Profile")
                print("7. Logout")

                emp_choice = input("Enter Your Choice: ")

                # 1. View Assigned Tasks
                if emp_choice == '1':

                    query = """
                        SELECT t.task_id, t.title, t.description,
                            t.priority, t.due_date, t.status
                        FROM tasks t
                        INNER JOIN assigned_tasks a
                        ON t.task_id = a.task_id
                        WHERE a.emp_id = %s
                    """

                    cur.execute(query, (emp_id,))
                    result = cur.fetchall()

                    if result:
                        print("\n========== MY ASSIGNED TASKS ==========")

                        for row in result:
                            print("Task ID:", row[0])
                            print("Title:", row[1])
                            print("Description:", row[2])
                            print("Priority:", row[3])
                            print("Due Date:", row[4])
                            print("Status:", row[5])
                            print("-----------------------------------")

                    else:
                        print("No assigned tasks found.")

                # 2. View Task Details
                elif emp_choice == '2':

                    task_id = int(input("Enter Task ID: "))

                    query = """
                        SELECT t.task_id, t.title, t.description,
                            t.priority, t.due_date, t.status,
                            t.created_at
                        FROM tasks t
                        INNER JOIN assigned_tasks a
                        ON t.task_id = a.task_id
                        WHERE t.task_id = %s AND a.emp_id = %s
                    """

                    cur.execute(query, (task_id, emp_id))
                    result = cur.fetchone()

                    if result:
                        print("\n========== TASK DETAILS ==========")
                        print("Task ID:", result[0])
                        print("Title:", result[1])
                        print("Description:", result[2])
                        print("Priority:", result[3])
                        print("Due Date:", result[4])
                        print("Status:", result[5])
                        print("Created At:", result[6])

                    else:
                        print("Task not found or not assigned to you.")

                # 3. Update Task Status
                elif emp_choice == '3':

                    task_id = int(input("Enter Task ID: "))

                    query = """
                        SELECT task_id
                        FROM assigned_tasks
                        WHERE task_id = %s AND emp_id = %s
                    """

                    cur.execute(query, (task_id, emp_id))
                    result = cur.fetchone()

                    if result:

                        print("\n1. Pending")
                        print("2. In Progress")
                        print("3. Completed")

                        status_choice = input("Select Task Status: ")

                        if status_choice == '1':
                            status = 'Pending'

                        elif status_choice == '2':
                            status = 'In Progress'

                        elif status_choice == '3':
                            status = 'Completed'

                        else:
                            print("Invalid Status Choice!")
                            continue

                        query = """
                            UPDATE tasks
                            SET status = %s
                            WHERE task_id = %s
                        """

                        cur.execute(query, (status, task_id))
                        con.commit()

                        print("Task Status Updated Successfully!")

                    else:
                        print("Task not found or not assigned to you.")

                # 4. Add Comments
                elif emp_choice == '4':

                    task_id = int(input("Enter Task ID: "))

                    query = """
                        SELECT task_id
                        FROM assigned_tasks
                        WHERE task_id = %s AND emp_id = %s
                    """

                    cur.execute(query, (task_id, emp_id))
                    result = cur.fetchone()

                    if result:

                        comment = input("Enter Your Comment: ")

                        cur.execute("SELECT MAX(c_id) FROM comments")
                        last_id = cur.fetchone()[0]
                        comment_id = 1 if last_id is None else last_id + 1

                        query = """
                            INSERT INTO comments
                            (c_id, task_id, emp_id, comment)
                            VALUES (%s, %s, %s, %s)
                        """

                        cur.execute(
                            query,
                            (comment_id, task_id, emp_id, comment)
                        )
                        con.commit()

                        print("Comment Added Successfully!")

                    else:
                        print("Task not found or not assigned to you.")

                # 5. View Completed Tasks
                elif emp_choice == '5':

                    query = """
                        SELECT t.task_id, t.title, t.description,
                            t.priority, t.due_date, t.status
                        FROM tasks t
                        INNER JOIN assigned_tasks a
                        ON t.task_id = a.task_id
                        WHERE a.emp_id = %s
                        AND t.status = 'Completed'
                    """

                    cur.execute(query, (emp_id,))
                    result = cur.fetchall()

                    if result:
                        print("\n========== COMPLETED TASKS ==========")

                        for row in result:
                            print("Task ID:", row[0])
                            print("Title:", row[1])
                            print("Description:", row[2])
                            print("Priority:", row[3])
                            print("Due Date:", row[4])
                            print("Status:", row[5])
                            print("-----------------------------------")

                    else:
                        print("No completed tasks found.")

                # 6. View Employee Profile
                elif emp_choice == '6':

                    query = """
                        SELECT *
                        FROM employees
                        WHERE Emp_id = %s
                    """

                    cur.execute(query, (emp_id,))
                    result = cur.fetchone()

                    if result:
                        print("\n========== MY PROFILE ==========")

                        columns = [desc[0] for desc in cur.description]

                        for column, value in zip(columns, result):
                            print(column, ":", value)

                    else:
                        print("Employee profile not found.")

                # 7. Logout
                elif emp_choice == '7':

                    print("Employee Logged Out Successfully!")
                    break

                else:
                    print("Invalid Choice! Please Try Again.")

        else:
            print("Employee not found.")



    elif choice == '3':
        print("Thank you for using the application")
        break

    else:
        print("Invalid Choice. Try Again")

