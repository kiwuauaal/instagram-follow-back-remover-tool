@echo off
cls
echo ========================================
echo Instagram Mutual-Follow Analyzer Setup
echo ========================================
echo.

echo Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python not found!
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Python found successfully!
echo.

echo Installing/upgrading pip...
python -m pip install --upgrade pip

echo.
echo Setup complete! You can now run:
echo python instagram_analyzer.py
echo.

pause