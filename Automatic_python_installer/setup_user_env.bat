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

:: ----------------------------
:: Ask user about installing Git
:: ----------------------------
echo You are now done with installing VScode, python, pip, pygame, selenium and numpy.
echo Now open VScode and make a python file, also install the python extension in the VScode editor.
echo If you want, you can choose if you want to install git (only if you are familiar with it).
echo Do you want to install Git? (Y/n)
set /p userChoice=Enter choice [Y/n]:

:: Check if the user entered 'y' or 'Y' (case-insensitive)
if /i "%userChoice%"=="y" (
    echo Installing Git...

    :: Download Git installer (silent installation)
    powershell -Command "Invoke-WebRequest -Uri https://github.com/git-for-windows/git/releases/download/v2.40.1.windows.1/Git-2.40.1-64-bit.exe -OutFile Git-Installer.exe"

    :: Run the installer silently (no user interaction)
    start /wait Git-Installer.exe /VERYSILENT /SUPPRESSMSGBOXES /NORESTART

    :: Add Git to the user PATH (without admin rights)
    echo Adding Git to the user PATH...
    setx PATH "%PATH%;C:\Users\%USERNAME%\AppData\Local\Programs\Git\cmd"

    :: Inform the user that Git is now installed
    echo Git has been installed and added to your PATH.
) else (
    echo Skipping Git installation...
)

:: ========================================
echo Setup complete (no admin needed)!
echo ========================================

pause
