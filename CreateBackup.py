import os
import platform
import zipfile
import time
from pathlib import Path
import subprocess
import platform

def get_color(indexer):
    return "\033[31m" if indexer == 1 else "\033[32m" if indexer == 2 else "\033[33m" if indexer == 3 else "\033[34m" if indexer == 4 else "\033[0m"
    
def get_time_seconds():
    return int(round(time.time()))
    
def open_folder(path):
    folder = Path(path).absolute()

    if platform.system() == "Windows":
        subprocess.run(["explorer", str(folder)])
    elif platform.system() == "Darwin":
        subprocess.run(["open", str(folder)])
    else:
        subprocess.run(["xdg-open", str(folder)])

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def list_folders(path):
    """List all folders in the given path"""
    try:
        return [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    except:
        return ""
        
def zip_folder(path):
    with zipfile.ZipFile(path + f"_{get_time_seconds()}" + ".zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, path)
                zipf.write(file_path, arcname)
                
def zip_folder_with_parent(path):
    folder_name = os.path.basename(path)
    
    with zipfile.ZipFile(path + f"_{get_time_seconds()}" + ".zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.join(folder_name, os.path.relpath(file_path, path))
                zipf.write(file_path, arcname)
    
savesPath = ""

#Get owner "username"
username = os.getenv('USERNAME') or os.getenv('USER')

if platform.system() == "Windows":
    savesPath = "C:\\Users\\" + username + "\\Zomboid\\Saves\\"
else:
    savesPath = "~\\Zomboid\\Saves\\"

saveType = 0
saveTypeStr = ""

clear_screen()

print("Welcome to this simple Zomboid save backup tool \nMade with love by NOSFYT, you can follow my github on: https://github.com/fjgimeno")

while(saveType < 1 or saveType > 5):
    try:
        saveType = int(input("\n\nPlease input the save type number: \n\t 1- Apocalypse \n\t 2- Survivor \n\t 3- Builder \n\t 4- Sandbox \n\t 5- Quit \n\n Input: "))
    except:
        print("Please enter a valid number between 1 and 5, both inclusive");

if(saveType == 5):
    print("\n\n\tSad to see you go. \n\n\tHappy gaming!\n\n")
    raise SystemExit

saveTypeStr = "Apocalypse" if saveType == 1 else "Survivor" if saveType == 2 else "Builder" if saveType == 3 else "Sandbox" if saveType == 4 else ""
    
if (saveTypeStr == ""):
    print(get_color(1) + "Wow something went incredibly wrong (ERR Code 001)." + get_color(0))
    input("\n\nPress enter to exit...")
    raise SystemExit(1)

savesPath = savesPath + saveTypeStr

clear_screen()

print("(if you don't know which folder it is, it's best if you rename your save in-game, press 'load' then select your save, then click on 'more...' finally change savefile name and click on  'Rename File', once done, re-launch this app)\n\n")

index = 0
folders = list_folders(savesPath);

selectedFolder = 0;
selectedFolderStr = ""
totalFolders = len(folders)

if(totalFolders == 0):
    print(get_color(1) + "Wow there champ, there are no saves of the  previously selected type (ERR Code 002)." + get_color(0))
    input("\n\nPress enter to exit...")
    raise SystemExit(1)

while(selectedFolder < 1 or selectedFolder > totalFolders):
    clear_screen()
    print(f"Number of saves:  {totalFolders}\n")

    index = 0
    for folder in folders:
        index += 1
        print(get_color(2) + f"\t{index}- " + folder + get_color(0))
    try:
        selectedFolder = int(input("\n\nPlease input the save index number: \n\t Input: "))
    except:
        clear_screen()
        print("Please enter a valid number");
        
selectedFolderStr = folders[selectedFolder -1]

clear_screen()
finalPath = savesPath + "\\" + selectedFolderStr
print("Folder to backup: " + finalPath)
print("\nProceding to ZIP the folder, this may take a while...\n\n\tZipping...")
zip_folder_with_parent(finalPath)

clear_screen()
print("File Zipping done! \n\n\tHappy Gaming!");
open_folder(savesPath)

input("\n\nPress enter to exit...")
