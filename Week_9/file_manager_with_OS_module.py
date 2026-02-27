import os

def file_manager():
    # Display the current working directory
    print(f"Current working directory: {os.getcwd()}\n")

    # Create a new folder called "lab_files"
    directory = "lab_files"
    parent_d = os.getcwd()
    path = os.path.join(parent_d, directory)
    if not os.path.exists(directory):
        os.mkdir(path)
        print(f"Directory '{directory}' created at: {path}\n")
    else:
        print(f"Directory '{directory}' already exists at: {path}\n")

    # Create three empty text files inside that folder
    files = ['new_file1.txt', 'new_file2.txt', 'new_file3.txt']
    for filename in files:
        file_path = os.path.join(path, filename)
        if not os.path.isfile(file_path):
            with open(file_path, 'w') as file:  # Fixed spacing
                file.write(f"This is {filename}\n")
            print(f"File '{filename}' created in directory '{directory}'")
        else:
            print(f"File '{filename}' already exists in directory '{directory}'")

    # List all files in the folder
    if len(os.listdir(directory)) == 0:
        print(f"\nDirectory '{directory}' is empty\n")
    else:
        print(f"\nAll files in '{directory}':")
        print(os.listdir(directory))
        print()

    # Rename one of the files
    source = os.path.join(directory, 'new_file3.txt')
    destination = os.path.join(directory, 'renamed_file3.txt')
    if not os.path.exists(source):
        print(f"Source file does not exist: {source}")
    elif os.path.exists(destination):
        print(f"Destination file already exists: {destination}")
    else:
        os.rename(source, destination)
        print(f"File '{source}' successfully renamed to '{destination}'\n")

    # Clean up by removing all files and the folder
    print(f"Removing all files in '{directory}':")
    for file in os.listdir(directory):
        file_loc = os.path.join(directory, file)
        os.remove(file_loc)
        print(f"File '{file}' removed from '{directory}'")

    print(f"\nRemoving directory: '{directory}'")
    os.rmdir(directory)
    print(f"Directory '{directory}' successfully removed\n")

    # Check that file and folder removal was successful
    try:
        print(f"All files in '{directory}':")
        print(os.listdir(directory))
    except OSError:
        print(f"Directory '{directory}' no longer exists\n")

file_manager()