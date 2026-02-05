import os
from PIL import Image

def convert_image():
    print("\n" + "="*40)
    print("      SCRIPT SAVANT: IMAGE CONVERTER")
    print("="*40)

    # 1. Get User Input for File
    file_path = input("\n🖼️ Enter the path of the image to convert: ").strip('"')
    
    if not os.path.exists(file_path):
        print("❌ Error: File not found!")
        return

    # 2. Define Supported Formats
    print("\nSupported Output Formats: PNG, JPG, JPEG, WEBP, BMP")
    target_ext = input("🎯 Enter target format (e.g., png, jpg): ").lower().replace(".", "")

    # 3. Handle naming and paths
    base_name = os.path.splitext(file_path)[0]
    # 'jpg' is often referred to as 'jpeg' in Pillow
    save_ext = "jpeg" if target_ext == "jpg" else target_ext
    output_path = f"{base_name}_converted.{target_ext}"

    try:
        with Image.open(file_path) as img:
            # Convert to RGB if saving as JPG (Pillow requirement for PNG/RGBA to JPG)
            if save_ext == "jpeg" and img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            
            img.save(output_path, save_ext.upper())
            print(f"\n✅ SUCCESS! Converted image saved as: {output_path}")
            
    except Exception as e:
        print(f"\n❌ ERROR: {e}")

if __name__ == "__main__":
    convert_image()
