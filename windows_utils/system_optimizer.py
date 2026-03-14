
import os
import shutil
import psutil
import tempfile
import time

def get_size(bytes_size, suffix="B"):
    """Converts bytes to a human-readable format (MB, GB, etc.)"""
    factor = 1024
    for unit in ["", "K", "M", "G", "T"]:
        if bytes_size < factor:
            return f"{bytes_size:.2f} {unit}{suffix}"
        bytes_size /= factor

def show_pc_health():
    print("\n--- 💻 System Health Dashboard ---")
    
    # CPU Usage
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"🧠 CPU Usage: {cpu_usage}%")
    
    # RAM Usage
    ram = psutil.virtual_memory()
    print(f"🐏 RAM Usage: {get_size(ram.used)} / {get_size(ram.total)} ({ram.percent}%)")
    
    # Disk Usage
    disk = psutil.disk_usage(os.path.abspath(os.sep))
    print(f"💾 Disk Space: {get_size(disk.free)} free out of {get_size(disk.total)} ({disk.percent}% used)")
    print("----------------------------------")

def clean_temp_files():
    print("\n--- 🗑️ System Temp Cleaner ---")
    # Get the path to the current user's Temp folder
    temp_dir = tempfile.gettempdir()
    print(f"🔍 Scanning: {temp_dir}")
    
    freed_space = 0
    deleted_files = 0
    deleted_folders = 0

    for item in os.listdir(temp_dir):
        item_path = os.path.join(temp_dir, item)
        try:
            # Calculate size before deleting
            size = os.path.getsize(item_path) if os.path.isfile(item_path) else 0
            
            if os.path.isfile(item_path):
                os.remove(item_path)
                deleted_files += 1
                freed_space += size
            elif os.path.isdir(item_path):
                # get tree size (approx)
                for dirpath, _, filenames in os.walk(item_path):
                    for f in filenames:
                        fp = os.path.join(dirpath, f)
                        if not os.path.islink(fp):
                            freed_space += os.path.getsize(fp)
                shutil.rmtree(item_path)
                deleted_folders += 1
                
        except Exception:
            # Files currently in use by Windows will throw an error, we simply skip them
            pass

    print(f"✅ SUCCESS! Cleared {deleted_files} files and {deleted_folders} folders.")
    print(f"🎉 Total Space Freed: {get_size(freed_space)}")

def main_menu():
    while True:
        print("\n" + "="*40)
        print("   SCRIPT SAVANT: SYSTEM OPTIMIZER")
        print("="*40)
        print("1. 💻 View PC Health Dashboard")
        print("2. 🗑️ Clean Temporary Files (Free up space)")
        print("0. 🚪 Exit")
        
        choice = input("\nEnter choice (0-2): ")
        
        if choice == '1': 
            show_pc_health()
        elif choice == '2': 
            clean_temp_files()
        elif choice == '0': 
            break
        else: 
            print("Invalid choice!")
            
        time.sleep(1) # Small pause for readability

if __name__ == "__main__":
    main_menu()
