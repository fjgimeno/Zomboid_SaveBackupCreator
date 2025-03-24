@echo off
REM Optimized Python executable builder
SET SCRIPT_NAME=CreateBackup.py
SET EXE_NAME=Zomboid_CreateBackup

echo Creating optimized build of %SCRIPT_NAME%...

REM Run PyInstaller with exclusions and optimizations
pyinstaller ^
    --onefile ^
    --console ^
    --clean ^
    --name %EXE_NAME% ^
    --exclude-module tkinter ^
    --exclude-module numpy ^
    --exclude-module pandas ^
    --exclude-module matplotlib ^
    --exclude-module unittest ^
    --exclude-module email ^
    --exclude-module http ^
    --exclude-module xml ^
    %SCRIPT_NAME%

echo Build complete! Executable is in the 'dist' folder.
pause