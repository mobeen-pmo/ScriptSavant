import os

def rename_with_prefix(folder_path):
    print("\n--- 🏷️ Prefix & Numbering Mode ---")
    prefix = input("Enter the new prefix (e.g., 'Vacation_Pic'): ")
    
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    if not files:
        print("❌ No files found in this directory.")
        return

    print(f"\n🔄 Renaming {len(files)} files...")
    
    count = 1
    for filename in files:
        file_ext = os.path.splitext(filename)[1]
        # Creates names like: Vacation_Pic_01.jpg
        new_name = f"{prefix}_{str(count).zfill(2)}{file_ext}"
        
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)
        
        try:
            os.rename(old_file, new_file)
            count += 1
        except Exception as e:
            print(f"⚠️ Could not rename {filename}: {e}")
            
    print(f"✅ SUCCESS! Renamed {count - 1} files.")

def rename_by_replace(folder_path):
    print("\n--- 🔍 Search & Replace Mode ---")
    search_text = input("Text to find in filenames (e.g., 'draft'): ")
    replace_text = input("Replace it with (e.g., 'final'): ")
    
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    count = 0
    for filename in files:
        if search_text in filename:
            new_name = filename.replace(search_text, replace_text)
            
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, new_name)
            
            try:
                os.rename(old_file, new_file)
                count += 1
            except Exception as e:
                print(f"⚠️ Could not rename {filename}: {e}")
                
    if count > 0:
        print(f"✅ SUCCESS! Updated {count} files.")
    else:
        print("ℹ️ No files found containing that text.")

def main_menu():
    print("\n" + "="*40)
    print("   SCRIPT SAVANT: BULK FILE RENAMER")
    print("="*40)
    
    folder_path = input("\n📂 Enter the folder path containing the files: ").strip('"')
    
    if not os.path.exists(folder_path):
        print("❌ Error: Directory does not exist!")
        return

    while True:
        print("\nChoose Renaming Mode:")
        print("1. 🏷️ Rename all with a Prefix & Number (e.g., Doc_01, Doc_02)")
        print("2. 🔍 Search and Replace specific words in filenames")
        print("0. 🚪 Exit")
        
        choice = input("\nEnter choice (0-2): ")
        
        if choice == '1': 
            rename_with_prefix(folder_path)
            break
        elif choice == '2': 
            rename_by_replace(folder_path)
            break
        elif choice == '0': 
            break
        else: 
            print("Invalid choice!")

if __name__ == "__main__":
    main_menu()
