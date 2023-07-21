import shutil
import os

# get all the files
items = os.listdir(".")
for item in items:
    # print(item.endswith("txt"))
    if item.endswith("txt"):
        try:
            os.mkdir("Text")
        except:
            print("Text files move to existing folder")
        current_file = "item"
        current_path = f"./{item}"
        shutil.move(current_path,"./Text")
    if item.endswith("mp3") or item.endswith("m4a"):
        try:
            os.mkdir("Music")
        except:
            print("Music files move to existing folder")
        current_file = "item"
        current_path = f"./{item}"
        shutil.move(current_path,"./Music")
    if item.endswith("mp4") or item.endswith("mkv") or item.endswith("3gp") or item.endswith("webm"):
        try:
            os.mkdir("Videos")
        except:
            print("Video files move to existing folder")
        current_file = "item"
        current_path = f"./{item}"
        shutil.move(current_path,"./Videos")
    if item.endswith("jpg") or item.endswith("png") or item.endswith("jpeg"):
        try:
            os.mkdir("Images")
        except:
            print("Image files move to existing folder")
        current_file = "item"
        current_path = f"./{item}"
        shutil.move(current_path,"./Images")
    
    if item.endswith("doc") or item.endswith("pdf") or item.endswith("docx"):
        try:
            os.mkdir("Documents")
        except:
            print("Documents files move to existing folder")
        current_file = "item"
        current_path = f"./{item}"
        shutil.move(current_path,"./Documents")
    if item.endswith("py") or item.endswith("java") or item.endswith("sql"):
        if item!="organiser.py":
            try:
                os.mkdir("Coding_files")
            except:
                print("Documents files move to existing folder")
            current_file = "item"
            current_path = f"./{item}"
            shutil.move(current_path,"./Coding_files")
    if item.endswith("exe") or item.endswith("msi"):
        try:
            os.mkdir("Executables")
        except:
            print("Executables files move to existing folder")
        current_file = "item"
        current_path = f"./{item}"
        shutil.move(current_path,"./Executables")