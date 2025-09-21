@echo off
echo Starting DermDetect Web App...
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install requirements
echo Installing dependencies...
pip install -r requirements.txt

REM Copy model file if it doesn't exist
if not exist "final_tinyvit_safe.pth" (
    echo.
    echo Please copy your model file to this directory:
    echo copy "E:\SkinCancerDetection\final_tinyvit_safe.pth" "final_tinyvit_safe.pth"
    echo.
    pause
)

REM Start the application
echo.
echo Starting web application...
echo Open your browser and go to: http://localhost:5000
echo.
python app.py

pause