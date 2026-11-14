# Project Report: Employee Attendance System

**Institution:** Rungta International Skills University  
**School:** School of Computer Science and Engineering  
**Course:** B.Tech / CSE / First Sem / Section – J  
**Subject:** Programming Fundamentals and Logic Building Using Python (`RU-100-01-0021`)  
**Problem Statement No.:** 35  
**Date of Allocation:** 14th October 2026  
**Date of Submission:** 16th November 2026  

---

## 1. Problem Definition

Organizations need a simple, reliable way to maintain daily attendance records for employees. The objective of this project is to build a menu-driven Python 3 console application that allows adding employees, marking their daily attendance as Present (`P`), Absent (`A`), or Leave (`L`), preventing invalid or duplicate entries, generating individual attendance reports, and persisting all data in `attendance.txt`.

---

## 2. Objectives

1. Assign unique sequential employee IDs starting from `E101`.
2. Store each employee as a dictionary (`id`, `name`, `records`) inside a Python list.
3. Validate employee IDs, date formats (`YYYY-MM-DD`), and attendance status codes (`P`, `A`, `L`).
4. Block duplicate attendance marking for the same employee on the same date.
5. Calculate attendance percentage using `Present days / marked days * 100`.
6. Load data automatically from `attendance.txt` on startup and save after every update.

---

## 3. Programming Concepts Used

- **Lists:** Maintain the collection of all employee dictionaries (`employees`).
- **Dictionaries:** Represent each employee (`{"id": ..., "name": ..., "records": {...}}`) and map dates to status codes (`{"2026-08-01": "P"}`).
- **Functions:** Modularize responsibilities into `load_data`, `save_data`, `generate_employee_id`, `find_employee`, `is_valid_date`, `is_valid_status`, `add_employee`, `mark_attendance`, `show_report`, and `view_all_employees`.
- **Conditional Statements & Loops:** Handle menu navigation, input validation, duplicate detection, and attendance counting.
- **File Handling:** Read from and write to `attendance.txt` using UTF-8 text format (`id|name|date:status,...`).

---

## 4. Data Storage Format (`attendance.txt`)

Each line in `attendance.txt` stores one employee in pipe-separated format:

```text
E101|Aman|2026-08-01:P,2026-08-02:P,2026-08-03:A,2026-08-04:L
```

---

## 5. System Workflow

1. **Startup:** `load_data()` reads `attendance.txt` (if present) and populates the `employees` list.
2. **Add Employee (Option 1):** Generates the next ID (`E101`, `E102`, ...), appends the dictionary to `employees`, and calls `save_data()`.
3. **Mark Attendance (Option 2):**
   - Verifies employee exists.
   - Validates date (`YYYY-MM-DD`).
   - Validates status (`P`, `A`, `L`).
   - Checks if the date is already present in `emp["records"]`.
   - Saves the attendance record and writes to `attendance.txt`.
4. **View Attendance Report (Option 3):** Counts `P`, `A`, and `L` entries and displays the percentage (or `0.00% (no records)` when empty).
5. **View All Employees (Option 4):** Lists all registered employees and their total marked days.
6. **Exit (Option 5):** Closes the application safely.

---

## 6. Test Cases & Verification Results

All four required test cases were executed sequentially on the same dataset and passed:

1. **Test Case 1 (Normal Input):**
   - Input: Option `1`, Name: `Aman`
   - Output: `Employee added: E101 | Aman` — **PASS**
2. **Test Case 2 (Boundary / Minimum Input):**
   - Input: Option `3`, ID: `E101` (with 0 records)
   - Output: `Aman: Present 0 | Absent 0 | Leave 0` and `Attendance: 0.00% (no records)` — **PASS**
3. **Test Case 3 (Invalid Input):**
   - (a) `E999`, `2026-08-01`, `P` → `Employee E999 not found.` — **PASS**
   - (b) `E101`, `2026-13-45`, `P` → `Invalid date. Use YYYY-MM-DD.` — **PASS**
   - (c) `E101`, `2026-08-01`, `X` → `Invalid status. Enter P, A or L.` — **PASS**
4. **Test Case 4 (Different Valid Scenario & Duplicate Check):**
   - Marked `2026-08-01 P`, `2026-08-02 P`, `2026-08-03 A`, `2026-08-04 L`, then repeated `2026-08-02 P`, then Option `3` for `E101`.
   - Output: `Attendance for 2026-08-02 is already marked.`, `Aman: Present 2 | Absent 1 | Leave 1`, `Attendance: 50.00%` — **PASS**

---

## 7. Conclusion

The Employee Attendance System satisfies all functional and validation requirements using core Python 3 constructs. The modular design ensures clean readability, persistent storage, and accurate attendance reporting.
