@echo off
SET SCRIPT_NAME=CreateBackup.py
SET EXE_NAME=Zomboid_CreateBackup
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
pause
