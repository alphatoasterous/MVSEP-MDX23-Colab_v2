:: This script was made for using this repository standalone. Please be aware that it is not the intended way of using
:: this software and additional fiddling may be required for making this work.

@echo off

:: Define paths
set "VIRTUALENV_DIR=.venv"
set "REQUIREMENTS_FILE=requirements_standalone.txt"
set "WEBUI_SCRIPT=webui.py"

:: Check if virtualenv directory exists
if exist "%VIRTUALENV_DIR%" (
    echo Virtualenv directory exists. Skipping dependency installation.
) else (
    pip install virtualenv
    if %errorlevel% neq 0 (
        echo Virtualenv installation failed. Concider installing it manually.
        pause>nul
        exit /B 1
    )
    echo Creating virtualenv...
    python -m virtualenv "%VIRTUALENV_DIR%"
    echo Installing dependencies...
    %VIRTUALENV_DIR%\Scripts\pip.exe install -r "%REQUIREMENTS_FILE%"
)

:: Activate virtualenv
call "%VIRTUALENV_DIR%\Scripts\activate"

:: Run python script
echo Starting Web UI...
python "%WEBUI_SCRIPT%"

:: Deactivate virtualenv
deactivate