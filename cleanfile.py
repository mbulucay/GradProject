import os

# folder path
dir_path = r'./'

# list to store files
files = []
folders = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        files.append(path)
    else:
        folders.append(path)

print(files)
print(folders)






