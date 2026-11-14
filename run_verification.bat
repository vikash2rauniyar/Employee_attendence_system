@echo off
title Testing Employee Attendance System (PS No. 35)
cd /d "%~dp0"
echo ========================================================
echo Checking Project with Official Test Cases...
echo ========================================================
python verify_test_cases.py
echo.
pause
