import os

def rename_file():
    i = 0 # for count the .txt 
    for  root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            file_path = os.path.join(root, file)

            if file_path.endswith('.txt'):
                i = i+1
                string = str(i)
                new_file_name = string + file_path[-4:]
                print new_file_name

                os.rename(file_path, new_file_name)

if __name__ == '__main__':
    rename_file()