"""
Employee Attendance System (PS No. 35)
B.Tech CSE - Programming Fundamentals and Logic Building Using Python (RU-100-01-0021)

A console application to add employees, mark daily attendance (Present, Absent, Leave),
and view attendance reports with persistent storage in attendance.txt.
"""

from datetime import datetime
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "attendance.txt")
VALID_STATUSES = ("P", "A", "L")


def load_data(filename=DATA_FILE):
    """Load employee records from the text file into a list of dictionaries."""
    employees = []
    if not os.path.exists(filename):
        return employees

    with open(filename, "r", encoding="utf-8") as file:
        for raw_line in file:
            line = raw_line.strip()
            if not line:
                continue

            parts = line.split("|", 2)
            if len(parts) < 2:
                continue

            emp_id = parts[0].strip()
            name = parts[1].strip()
            records = {}

            if len(parts) == 3 and parts[2].strip():
                for entry in parts[2].split(","):
                    if ":" in entry:
                        date_str, status = entry.split(":", 1)
                        records[date_str.strip()] = status.strip()

            employees.append({
                "id": emp_id,
                "name": name,
                "records": records,
            })

    return employees


def save_data(employees, filename=DATA_FILE):
    """Save all employee records from the list of dictionaries to the text file."""
    with open(filename, "w", encoding="utf-8") as file:
        for emp in employees:
            sorted_dates = sorted(emp["records"].keys())
            record_str = ",".join(
                f"{date_str}:{emp['records'][date_str]}" for date_str in sorted_dates
            )
            file.write(f"{emp['id']}|{emp['name']}|{record_str}\n")


def generate_employee_id(employees):
    """Generate the next sequential employee ID starting from E101."""
    if not employees:
        return "E101"

    max_num = 100
    for emp in employees:
        emp_id = emp["id"]
        if emp_id.startswith("E") and emp_id[1:].isdigit():
            max_num = max(max_num, int(emp_id[1:]))
    return f"E{max_num + 1}"


def find_employee(employees, emp_id):
    """Find and return an employee dictionary by ID, or None if not found."""
    target_id = emp_id.strip().upper()
    for emp in employees:
        if emp["id"].upper() == target_id:
            return emp
    return None


def is_valid_date(date_str):
    """Validate that date_str strictly matches YYYY-MM-DD and is a real calendar date."""
    if len(date_str) != 10 or date_str[4] != "-" or date_str[7] != "-":
        return False
    year_part, month_part, day_part = date_str.split("-")
    if not (year_part.isdigit() and month_part.isdigit() and day_part.isdigit()):
        return False
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def is_valid_status(status):
    """Check whether status is one of P (Present), A (Absent), or L (Leave)."""
    return status in VALID_STATUSES


def add_employee(employees, name):
    """Add a new employee with a generated ID and save to file."""
    clean_name = name.strip().replace("|", " ")
    if not clean_name:
        print("Employee name cannot be empty.")
        return None

    emp_id = generate_employee_id(employees)
    new_employee = {
        "id": emp_id,
        "name": clean_name,
        "records": {},
    }
    employees.append(new_employee)
    save_data(employees)
    print(f"Employee added: {emp_id} | {clean_name}")
    return new_employee


def mark_attendance(employees, emp_id, date_str, status):
    """Validate inputs, block duplicates, mark attendance, and save to file."""
    clean_id = emp_id.strip().upper()
    clean_date = date_str.strip()
    clean_status = status.strip().upper()

    emp = find_employee(employees, clean_id)
    if emp is None:
        print(f"Employee {clean_id} not found.")
        return False

    if not is_valid_date(clean_date):
        print("Invalid date. Use YYYY-MM-DD.")
        return False

    if not is_valid_status(clean_status):
        print("Invalid status. Enter P, A or L.")
        return False

    if clean_date in emp["records"]:
        print(f"Attendance for {clean_date} is already marked.")
        return False

    emp["records"][clean_date] = clean_status
    save_data(employees)
    print(f"Attendance marked: {emp['id']} | {clean_date} | {clean_status}")
    return True


def show_report(employees, emp_id):
    """Display attendance counts and percentage for a given employee."""
    clean_id = emp_id.strip().upper()
    emp = find_employee(employees, clean_id)
    if emp is None:
        print(f"Employee {clean_id} not found.")
        return False

    records = emp["records"]
    present_days = 0
    absent_days = 0
    leave_days = 0

    for status in records.values():
        if status == "P":
            present_days += 1
        elif status == "A":
            absent_days += 1
        elif status == "L":
            leave_days += 1

    total_marked = len(records)
    print(f"{emp['name']}: Present {present_days} | Absent {absent_days} | Leave {leave_days}")

    if total_marked == 0:
        print("Attendance: 0.00% (no records)")
    else:
        percentage = (present_days / total_marked) * 100
        print(f"Attendance: {percentage:.2f}%")
    return True


def view_all_employees(employees):
    """Display a summary list of all employees."""
    if not employees:
        print("No employees found.")
        return

    print("\n--- Registered Employees ---")
    for emp in employees:
        print(f"{emp['id']} | {emp['name']} | Marked Days: {len(emp['records'])}")


def display_menu():
    """Print the console application menu."""
    print("\n=== Employee Attendance System ===")
    print("1. Add Employee")
    print("2. Mark Attendance")
    print("3. View Attendance Report")
    print("4. View All Employees")
    print("5. Exit")


def main():
    """Run the interactive console loop."""
    employees = load_data()

    while True:
        display_menu()
        try:
            choice = input("Enter your choice (1-5): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting Employee Attendance System.")
            break

        if choice == "1":
            name = input("Enter employee name: ")
            add_employee(employees, name)
        elif choice == "2":
            emp_id = input("Enter employee ID (e.g., E101): ")
            date_str = input("Enter date (YYYY-MM-DD): ")
            status = input("Enter status (P/A/L): ")
            mark_attendance(employees, emp_id, date_str, status)
        elif choice == "3":
            emp_id = input("Enter employee ID (e.g., E101): ")
            show_report(employees, emp_id)
        elif choice == "4":
            view_all_employees(employees)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
