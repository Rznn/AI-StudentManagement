@echo off
echo Installing packages...
python -m pip install -r requirements.txt
pause
cls
python app.py