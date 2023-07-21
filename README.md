# File Organizer CLI App

The File Organizer CLI App is a simple command-line tool that helps you organize your files by moving them into specific folders based on their file types. It automatically detects the file type and moves it to the corresponding folder, making it easy to keep your files organized and clutter-free.

## How to Use

1. Make sure you have Python installed on your system.

2. Clone or download the repository to your local machine.

3. Open a terminal or command prompt and navigate to the directory containing the organizer.py file.

4. To run the file organizer, execute the following command:

```bash
python organiser.py
```

5. The app will scan the current directory for files and move them to appropriate folders based on their types.

## Supported File Types and Destination Folders

- Text files (ending with .txt): Stored in the "Text" folder.
- Music files (ending with .mp3): Stored in the "Music" folder.
- Video files (ending with .mp4): Stored in the "Videos" folder.
- Image files (ending with .jpg, .jpeg, or .png): Stored in the "Images" folder.
- Document files (ending with .doc, .docx, or .pdf): Stored in the "Documents" folder.
- Coding files (ending with .py, .java, or .sql): Stored in the "Coding_files" folder.

Please note:

- If any of the destination folders already exist, the app will move the files to those existing folders.
- If a file doesn't match any of the supported file types, it will remain in the root directory.

<h1>IMPORTANT:</h1>
 Before running the organizer, ensure that you have the necessary permissions to read the files in the current directory and write/move files into the target folders.
<br>
<br>
<h1>Customization</h1>
You can customize the supported file types and destination folders by modifying the organizer.py file. Look for the if statements that check the file extensions, and adjust the conditions and destination folder names as needed.