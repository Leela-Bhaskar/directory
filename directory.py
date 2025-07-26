import os
import shutil

def organize_directory(path):
    """
    Organizes files in a given directory into subfolders based on file type.

    :param path: The absolute path of the directory to organize.
    """
    if not os.path.isdir(path):
        print(f"Error: Directory not found at '{path}'")
        return

    # --- Configuration: Define file types and their corresponding folders ---
    # You can customize these categories and add more file extensions.
    FILE_TYPE_MAPPING = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".ppt", ".pptx"],
        "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
        "Video": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Scripts": [".py", ".js", ".sh", ".bat", ".html", ".css"],
        "Executables": [".exe", ".msi", ".dmg"]
    }

    # --- Script Logic ---
    print(f"Starting to organize files in: {path}\n")

    # Get a list of all files in the directory
    try:
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    except OSError as e:
        print(f"Error reading directory: {e}")
        return

    # Iterate over each file and move it to the correct folder
    for file in files:
        file_moved = False
        # Find the file's extension
        file_extension = os.path.splitext(file)[1].lower()

        # Check which category the file belongs to
        for folder_name, extensions in FILE_TYPE_MAPPING.items():
            if file_extension in extensions:
                # Create the destination folder if it doesn't exist
                destination_folder_path = os.path.join(path, folder_name)
                os.makedirs(destination_folder_path, exist_ok=True)

                # Construct source and destination paths
                source_file_path = os.path.join(path, file)
                destination_file_path = os.path.join(destination_folder_path, file)

                # Move the file
                try:
                    shutil.move(source_file_path, destination_file_path)
                    print(f"Moved: '{file}' -> '{folder_name}/'")
                    file_moved = True
                    break # Move to the next file
                except (shutil.Error, OSError) as e:
                    print(f"Error moving '{file}': {e}")
                    # This can happen if a file with the same name already exists
                    # or due to permission issues.
                    file_moved = True # Treat as handled
                    break

        # If the file type is not in our mapping, move it to an 'Other' folder
        if not file_moved:
            other_folder_path = os.path.join(path, "Other")
            os.makedirs(other_folder_path, exist_ok=True)

            source_file_path = os.path.join(path, file)
            destination_file_path = os.path.join(other_folder_path, file)

            try:
                shutil.move(source_file_path, destination_file_path)
                print(f"Moved: '{file}' -> 'Other/'")
            except (shutil.Error, OSError) as e:
                print(f"Error moving '{file}' to 'Other/': {e}")


    print("\nFile organization complete.")

if __name__ == '__main__':
    # --- IMPORTANT ---
    # Replace this with the actual path to the directory you want to organize.
    # For example: "C:/Users/YourUsername/Downloads" on Windows
    # or "/Users/YourUsername/Downloads" on macOS/Linux.
    # Using a raw string (r"...") or double backslashes ("\\") on Windows is recommended.
    target_directory = r"C:\Users\leela\Downloads"

    organize_directory(target_directory)
