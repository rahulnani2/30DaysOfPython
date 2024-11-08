import os
folderList = input("""Enter the list of directories to list 
                   the files with spaces in between each dir""").split()

for folder in folderList:
    try:
        files = os.listdir(folderList)

    except FileNotFoundError:
        print("Input folder is Invalid :" , folder)
        continue
    except PermissionError:
        print("Permission Denied for the folder :", folder)
        continue
    for file in files:
        print(file)
