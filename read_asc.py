import os

# Set the directory path to iterate through
dir_path = './asc'
save_path = './text_data'

# Loop through all files in the directory
for file_name in os.listdir(dir_path):

    # Check if the current item is a file
    if os.path.isfile(os.path.join(dir_path, file_name)) and os.path.join(dir_path, file_name).format().endswith("asc"):
        # Process the file here, e.g. print its name
        print(os.path.join(dir_path, file_name).replace(".asc",""))
        
        with open(os.path.join(dir_path, file_name)) as f:
            lines = f.readlines()
        
        mag_data = []
        [mag_data.append(x.replace('\n','')) for x in lines[64:]]

        with open(os.path.join(save_path, file_name.replace(".asc", ".txt")), 'w') as f:
            for nth,data in enumerate(mag_data):
                f.write(data)
                if(nth+1 != len(mag_data)):
                    f.write(' ')
