# Employee Attendance System (PS No. 35)

**University:** Rungta International Skills University — School of Computer Science and Engineering  
**Program:** B.Tech / CSE / First Sem / Section – J  
**Course:** Programming Fundamentals and Logic Building Using Python (`RU-100-01-0021`)  
**Language:** Python 3  

## Problem Statement

Build a console application to add employees, mark their daily attendance as Present (`P`), Absent (`A`), or Leave (`L`), and view an attendance report for each employee. All employee and attendance data is saved persistently to `attendance.txt`.

## Features

- **Auto-generated Employee IDs:** Starts from `E101` (`E101`, `E102`, ...).
- **In-Memory Structure:** Stores each employee as a dictionary (`id`, `name`, `records`) inside a list.
- **Input Validation:**
  - Checks if employee ID exists before marking attendance or generating reports.
  - Validates dates strictly in `YYYY-MM-DD` format.
  - Validates attendance status (`P`, `A`, or `L`).
  - Blocks duplicate attendance entries for the same employee on the same date.
- **Persistent Storage:** Automatically loads data from `attendance.txt` at startup and saves after every change.
- **Attendance Report:** Displays counts of Present, Absent, and Leave days along with Attendance Percentage (`Present days / marked days * 100`).

## Project Files

- `employee_attendance.py` — Main Python 3 console application.
- `attendance.txt` — Text file storing employee and attendance records.
- `Project_Report.md` — Detailed project documentation and test report.
- `README.md` — Project overview and usage instructions.

## How to Run

1. Open Command Prompt / PowerShell in the project folder.
2. Run:
   ```bash
   python employee_attendance.py
   ```
3. Choose an option from the menu (`1` to `5`).

## Sample Test Cases

| Test Case | Input | Expected Output |
| :--- | :--- | :--- |
| **1. Normal Input** | Option `1`, Name: `Aman` | `Employee added: E101 | Aman` |
| **2. Boundary / Minimum** | Option `3`, ID: `E101` (no records) | `Aman: Present 0 | Absent 0 | Leave 0`<br>`Attendance: 0.00% (no records)` |
| **3a. Invalid Employee** | Option `2`, `E999`, `2026-08-01`, `P` | `Employee E999 not found.` |
| **3b. Invalid Date** | Option `2`, `E101`, `2026-13-45`, `P` | `Invalid date. Use YYYY-MM-DD.` |
| **3c. Invalid Status** | Option `2`, `E101`, `2026-08-01`, `X` | `Invalid status. Enter P, A or L.` |
| **4. Valid & Duplicate** | Mark `2026-08-01 P`, `2026-08-02 P`, `2026-08-03 A`, `2026-08-04 L`, duplicate `2026-08-02 P`, then Option `3`: `E101` | `Attendance for 2026-08-02 is already marked.`<br>`Aman: Present 2 | Absent 1 | Leave 1`<br>`Attendance: 50.00%` |
