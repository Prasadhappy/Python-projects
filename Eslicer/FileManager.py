import os
import shutil

def list_directory(path):
    print(f"\n📁 Contents of {path}: ")
    for item in os.listdir(path):
        print(" -", item)

def create_file(path, filename):
    full_path = os.path.join(path, filename)
    with open(full_path, 'w') as f:
        f.write("")  #creates an empty file

    print(f"File created: {full_path}")

def delete_file(path, filename):
    full_path = os.path.join(path, filename)
    if os.path.isfile(full_path):
        os.remove(full_path)
        print(f"file deleted: {full_path}")
    else:
        print("file not found")

def create_folder(path, foldername):
    full_path = os.path.join(path, foldername)
    os.makedirs(full_path, exist_ok = True)
    print(f"File created: {full_path}")

def delete_folder(path, foldername):
    full_path = os.path.join(path, foldername)
    if os.path.isdir(full_path):
        shutil.rmtree(full_path)
        print(f"Folder deleted: {full_path}")
    else:
        print("Folder not found")

def read_file(path, filename):
    full_path = os.path.join(path, filename)
    if os.path.isfile(full_path):
        with open(full_path, 'r') as f:
            print(f'\n Contents of {filename}: \n')
            print(f.read())

    else:
        print("File not found.")

def main():
    current_path = os.getcwd()
    print(f"Starting in directory: {current_path}")

    while True:
        print("\n Choose an action: ")
        print("1. List Directory")
        print("2. Create File")
        print("3. Delete File")
        print("4. Create Folder")
        print("5. Delete Folder")
        print("6. Read File")
        print("7. Change Directory")
        print("8. Exit")

        choice = input("Enter your choice(1-8): ")

        if choice == '1':
            list_directory(current_path)
        elif choice == '2':
            filename = input("Enter filename to create: ")
            create_file(current_path, filename)
        elif choice == '3':
            filename = input("Enter filename to delete: ")
            delete_file(current_path, filename)
        elif choice == '4':
            foldername = input("Enter Folder name to create: ")
            create_folder(current_path, foldername)
        elif choice == '5':
            foldername = input("Enter Folder name to delete: ")
            delete_folder(current_path, foldername)
        elif choice == '6':
            filename = input("Enter File name to read: ")
            read_file(current_path, filename)
        elif choice == '7':
            new_path = print("Enter new directory path: ")
            if os.path.isdir(new_path):
                current_path = new_path
                print(f"Changed directory to {current_path}")
            else:
                print("Invalid Directory")

        elif choice == '8':
            print("Exiting File Manager, Goodbye!")
            break
        else:
            print("invalid choice, please try again later")

if __name__  == "__main__":
    main()