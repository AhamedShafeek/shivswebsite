@echo off
echo ================================
echo Shiv's Photography Backend Setup
echo ================================
echo.

echo Installing Python dependencies...
pip install -r requirements.txt

echo.
echo ================================
echo Setup Complete!
echo ================================
echo.
echo To start the server, run:
echo   python app.py
echo.
echo Then open your browser and go to:
echo   http://localhost:5000
echo.
pause
