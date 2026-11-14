"""
Verification script for PS No. 35 - Employee Attendance System
Runs all 4 official assignment test cases and checks the outputs automatically.
"""

import subprocess
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MAIN_SCRIPT = os.path.join(SCRIPT_DIR, "employee_attendance.py")
DATA_FILE = os.path.join(SCRIPT_DIR, "attendance.txt")

def run_test():
    print("=" * 60)
    print(" RUNNING AUTOMATIC TEST CASES (RU PS No. 35) ")
    print("=" * 60)

    # 1. Clear attendance.txt for fresh test run
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            f.write("")

    # Sequence of user inputs to test all 4 cases:
    # TC 1: Option 1 -> Name: Aman
    # TC 2: Option 3 -> ID: E101
    # TC 3a: Option 2 -> E999, 2026-08-01, P
    # TC 3b: Option 2 -> E101, 2026-13-45, P
    # TC 3c: Option 2 -> E101, 2026-08-01, X
    # TC 4: Option 2 -> 2026-08-01 P
    #       Option 2 -> 2026-08-02 P
    #       Option 2 -> 2026-08-03 A
    #       Option 2 -> 2026-08-04 L
    #       Option 2 -> 2026-08-02 P (duplicate)
    #       Option 3 -> E101 (Report)
    # Exit: Option 5
    test_inputs = "\n".join([
        "1", "Aman",                          # TC 1
        "3", "E101",                          # TC 2
        "2", "E999", "2026-08-01", "P",       # TC 3a
        "2", "E101", "2026-13-45", "P",       # TC 3b
        "2", "E101", "2026-08-01", "X",       # TC 3c
        "2", "E101", "2026-08-01", "P",       # TC 4 mark 1
        "2", "E101", "2026-08-02", "P",       # TC 4 mark 2
        "2", "E101", "2026-08-03", "A",       # TC 4 mark 3
        "2", "E101", "2026-08-04", "L",       # TC 4 mark 4
        "2", "E101", "2026-08-02", "P",       # TC 4 duplicate test
        "3", "E101",                          # TC 4 view report
        "5"                                   # Exit
    ]) + "\n"

    proc = subprocess.run(
        [sys.executable, MAIN_SCRIPT],
        input=test_inputs,
        text=True,
        capture_output=True,
        encoding="utf-8"
    )

    output = proc.stdout
    errors = proc.stderr

    if proc.returncode != 0:
        print("[FAIL] Program crashed with error:")
        print(errors)
        return False

    checks = [
        ("Test Case 1: Add Employee Aman -> E101", "Employee added: E101 | Aman"),
        ("Test Case 2: Zero Attendance Report", "Aman: Present 0 | Absent 0 | Leave 0"),
        ("Test Case 2: Zero Percentage", "Attendance: 0.00% (no records)"),
        ("Test Case 3a: Non-existent Employee", "Employee E999 not found."),
        ("Test Case 3b: Invalid Date Format", "Invalid date. Use YYYY-MM-DD."),
        ("Test Case 3c: Invalid Status Code", "Invalid status. Enter P, A or L."),
        ("Test Case 4: Duplicate Date Blocked", "Attendance for 2026-08-02 is already marked."),
        ("Test Case 4: Final Attendance Counts", "Aman: Present 2 | Absent 1 | Leave 1"),
        ("Test Case 4: Final Attendance %", "Attendance: 50.00%"),
    ]

    all_passed = True
    print("\n--- TEST CASE VERIFICATION RESULTS ---")
    for description, expected in checks:
        if expected in output:
            print(f" [PASS] {description}")
        else:
            print(f" [FAIL] {description}")
            print(f"        Expected snippet: {expected}")
            all_passed = False

    # Check file persistence
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        file_content = f.read().strip()

    expected_file_line = "E101|Aman|2026-08-01:P,2026-08-02:P,2026-08-03:A,2026-08-04:L"
    if expected_file_line in file_content:
        print(f" [PASS] File Persistence: Data correctly saved to attendance.txt")
    else:
        print(f" [FAIL] File Persistence: attendance.txt content mismatch.")
        print(f"        Found: {file_content}")
        all_passed = False

    # Reset attendance.txt to clean state after test
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        f.write("")

    print("=" * 60)
    if all_passed:
        print(" RESULT: ALL TEST CASES PASSED! PROJECT 100% CORRECT HAI! ")
    else:
        print(" RESULT: SOME TESTS FAILED. PLEASE CHECK OUTPUT. ")
    print("=" * 60)
    return all_passed

if __name__ == "__main__":
    run_test()
