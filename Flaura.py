import os
import shutil
print ("🌸 Flora on the wat to bring digital calm to your chaotic folders ☺️ ☺️ 🌸")
# 📁 Step 1: Ask for the folder location and check if it exists
target_folder = input("📂 Enter location of the folder to organize:\n> ").strip()

# 🔍 Validate path
if not os.path.exists(target_folder):
    print("❌ The folder path you entered does not exist. Please check and try again.")
    exit()

# 📂 Step 2: Define categories and their file extensions
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".exe", ".msi", ".apk", ".bat", ".sh"],
    "Others": []  # Files that don't match any above
}

# 📌 Step 3: Create category folders if they don’t exist
for folder in file_types.keys():
    folder_path = os.path.join(target_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# 🚚 Step 4: Move files to corresponding folders
for filename in os.listdir(target_folder):
    file_path = os.path.join(target_folder, filename)
    if os.path.isfile(file_path):
        moved = False
        for folder_name, extensions in file_types.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                dest_path = os.path.join(target_folder, folder_name, filename)
                shutil.move(file_path, dest_path)
                print(f"✅ Moved: {filename} → {folder_name}")
                moved = True
                break
        if not moved:
            # If file extension doesn't match any, move to 'Others'
            dest_path = os.path.join(target_folder, "Others", filename)
            shutil.move(file_path, dest_path)
            print(f"✅ Moved: {filename} → Others")

print("\n🎉 All files organized successfully!")
