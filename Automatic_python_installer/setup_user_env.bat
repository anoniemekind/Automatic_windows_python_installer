@echo off
echo ========================================
echo Setting up DEV environment (no admin)...
echo ========================================

:: Create a temp working folder
set WORKDIR=%USERPROFILE%\dev_setup
mkdir "%WORKDIR%" 2>nul
cd /d "%WORKDIR%"

:: ----------------------------
:: Install Python (user mode)
:: ----------------------------
echo Downloading Python 3.12 installer...

curl -L -o python_installer.exe https://www.python.org/ftp/python/3.12.7/python-3.12.7-amd64.exe

echo Installing Python (user install)...
python_installer.exe /quiet InstallAllUsers=0 PrependPath=1 Include_test=0

:: Give it time to finish
timeout /t 10 >nul

:: Refresh PATH for current session
set PATH=%LOCALAPPDATA%\Programs\Python\Python312\;%LOCALAPPDATA%\Programs\Python\Python312\Scripts\;%PATH%

echo Checking Python...
python --version

:: ----------------------------
:: Ensure pip
:: ----------------------------
echo Ensuring pip...
python -m ensurepip --upgrade

echo Upgrading pip...
python -m pip install --upgrade pip

:: ----------------------------
:: Install libraries
:: ----------------------------
echo Installing pygame and selenium...
pip install --user pygame selenium numpy

:: ----------------------------
:: Install VS Code (user mode)
:: ----------------------------
echo Downloading VS Code...

curl -L -o vscode_installer.exe https://update.code.visualstudio.com/latest/win32-x64-user/stable

echo Installing VS Code (user install)...
vscode_installer.exe /verysilent /mergetasks=!runcode

echo ========================================
echo Setup complete (no admin needed)!
echo ========================================
pause