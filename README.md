# directory
File Organizer Script
A simple yet powerful Python script to automatically organize files in a directory (like your Downloads folder) into subdirectories based on their file type.

Description
This script scans a specified directory and moves files into categorized folders such as "Images," "Documents," "Video," "Audio," etc. This helps in decluttering folders that accumulate a lot of files of different types over time. Any file type that is not recognized will be moved into a separate "Other" folder.

Features
Automatic Sorting: Sorts files into folders based on their extension.

Easy to Customize: You can easily add new file types or change the folder structure by editing the script.

Safe: Creates destination folders if they don't exist. It will print an error if it cannot move a file (e.g., if a file with the same name already exists in the destination).

Cross-Platform: Works on Windows, macOS, and Linux.

Requirements
Python 3.x

No external libraries are needed; this script only uses Python's built-in os and shutil modules.

How to Use
Download the Script:
Save the code as a Python file, for example, organize.py.

Set the Target Directory:
This is the most important step. Open the organize.py script in a text editor and find this line at the bottom:

target_directory = r"YOUR_DIRECTORY_PATH_HERE"

Replace YOUR_DIRECTORY_PATH_HERE with the absolute path to the folder you want to organize.

Examples:

Windows: target_directory = r"C:\Users\YourUsername\Downloads"

macOS / Linux: target_directory = "/Users/YourUsername/Downloads"

Note for Windows users: Using the r before the string (like r"C:\...") is important as it prevents the backslashes from being misinterpreted.

Run the Script:
Open a terminal or command prompt, navigate to where you saved organize.py, and run it with the following command:

python organize.py

The script will then print the actions it's taking as it moves the files.

Customization
You can easily change which file types go into which folders. Open the script and find the FILE_TYPE_MAPPING dictionary near the top:

FILE_TYPE_MAPPING = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ...],
    "Documents": [".pdf", ".doc", ".docx", ...],
    # ... and so on
}

To add a new file extension: Add the extension (e.g., .ai) to one of the existing lists.

To add a new category: Add a new key-value pair to the dictionary (e.g., "Design Files": [".psd", ".ai", ".fig"]). The script will automatically create a folder with the new name.

License
This project is open-source. You can consider adding a license like the MIT License to let others know how they can use your code.
