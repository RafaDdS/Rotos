@echo off
echo.
echo Hallo meine Freund, this will configure everything in the virtual env XD
echo.
pause XD
echo.
echo initiate creation of virtual environment
echo.
python -m venv env
echo virtual environment created
echo.
call .\env\Scripts\activate
echo virtual env active
echo.
echo initiate search for dependances
echo.
pip install -r requirements.txt
echo.
echo dependances installed
echo.
echo everything done, bailing out
echo.
pause XD