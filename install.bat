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
echo initiate MATRIX (Neo, dont read this)
echo.
call .\env\Scripts\activate
echo MATRIX activated
echo.
echo initiate search for dependances
echo.
python -m pip install --upgrade pip
pip install -r requirements.txt
echo.
echo dependances installed
echo.
echo everything done, bailing out
echo.
pause XD
