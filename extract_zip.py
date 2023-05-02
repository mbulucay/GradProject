import os
import zipfile

# folder path
dir_path = r'./MARMARA AFAD DATA'

# list to store files
files = []
folders = []

# Iterate directory
for path in os.listdir(dir_path):
    
    # check if current path is a file
    print(path)

    for added_path in os.listdir(dir_path + "/" + path):

        if (added_path.format().endswith("zip")):
            print("     ", added_path + "   " + str(added_path.format().endswith("zip")))
            with zipfile.ZipFile(dir_path + "/" + path + "/" + added_path,"r") as zip_ref:
                zip_ref.extractall("./asc")
            
print(files)
print(folders)






