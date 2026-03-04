import os
import shutil
# Dictionary mapping folder names to their file extensions
FILE_CATEGORIES = {
    '🖼️ Images': ['.jpeg', '.jpg', '.png', '.gif', '.webp', '.bmp', '.svg', '.ico'],
    '📄 Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.csv', '.pptx', '.log'],
    '🎥 Videos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv'],
    '🎵 Audio': ['.mp3', '.wav', '.aac', '.flac'],
    '📦 Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    '⚙️ Installers': ['.exe', '.msi', '.apk', '.dmg'],
    '💻 Code': ['.py', '.html', '.css', '.js', '.json', '.cpp', '.java']
}

def get_category(extension):
    """Finds the right category folder for a given extension."""
    for folder, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return folder
    return '📁 Others'

def organize_directory():
    print("\n" + "="*40)
    print("   SCRIPT SAVANT: SMART FILE ORGANIZER")
    print("="*40)
    
    target_dir = input("\n📂 Enter the folder path to organize (e.g., C:/Users/Name/Downloads): ").strip('"')
    
    if not os.path.exists(target_dir):
        print("❌ Error: Directory does not exist!")
        return

    print(f"\n🔄 Scanning {target_dir}...")
    
    moved_count = 0
    # Loop through every item in the directory
    for item in os.listdir(target_dir):
        item_path = os.path.join(target_dir, item)
        
        # Skip directories, only process files
        if os.path.isdir(item_path):
            continue
            
        # Extract the file extension
        _, file_ext = os.path.splitext(item)
        file_ext = file_ext.lower()
        
        # Identify the correct folder based on the extension
        folder_name = get_category(file_ext)
        destination_folder = os.path.join(target_dir, folder_name)
        
        # Create the category folder if it doesn't exist
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
            
        # Move the file
        try:
            shutil.move(item_path, os.path.join(destination_folder, item))
            moved_count += 1
        except Exception as e:
            print(f"⚠️ Could not move {item}: {e} (File might be open or in use)")

    print(f"\n✅ SUCCESS! Organized {moved_count} files into their proper folders.")

if __name__ == "__main__":
    organize_directory()
