import os

def list_files(folders_list):
     for folder in folders_list:
        try:
            files = os.listdir(folders_list)
        except FileNotFoundError:
            print("Directory not found ! Enter a valid dir " + folder)
            continue
        except PermissionError:
            print("Permission denied to fodler " +  folder )
            continue
        for file in files:
            print(file)
 

folderList = input("""Enter the list of directories to list 
                   the files with spaces in between each dir""").split()
list_files(folderList)