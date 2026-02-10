import os
import pandas as pd
from pdf2docx import Converter
from docx2pdf import convert
from pdf2image import convert_from_path
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def word_to_pdf():
    print("\n--- 📄 Word (DOCX) to PDF ---")
    docx_file = input("Enter path to DOCX file: ").strip('"')
    if not os.path.exists(docx_file):
        print("❌ File not found!")
        return
    
    try:
        print("🔄 Converting...")
        convert(docx_file)
        print(f"✅ Success! PDF saved in the same folder.")
    except Exception as e:
        print(f"❌ Error: {e}")

def pdf_to_word():
    print("\n--- 📝 PDF to Word (DOCX) ---")
    pdf_file = input("Enter path to PDF file: ").strip('"')
    docx_file = os.path.splitext(pdf_file)[0] + ".docx"
    
    try:
        print("🔄 Converting...")
        cv = Converter(pdf_file)
        cv.convert(docx_file, start=0, end=None)
        cv.close()
        print(f"✅ Success! Saved as: {docx_file}")
    except Exception as e:
        print(f"❌ Error: {e}")

def excel_csv_converter(direction):
    if direction == "to_csv":
        print("\n--- 📊 Excel (XLSX) to CSV ---")
        src_file = input("Enter path to XLSX file: ").strip('"')
        dest_file = os.path.splitext(src_file)[0] + ".csv"
        read_func = pd.read_excel
        write_func = lambda df, f: df.to_csv(f, index=False)
    else:
        print("\n--- 📈 CSV to Excel (XLSX) ---")
        src_file = input("Enter path to CSV file: ").strip('"')
        dest_file = os.path.splitext(src_file)[0] + ".xlsx"
        read_func = pd.read_csv
        write_func = lambda df, f: df.to_excel(f, index=False)

    try:
        print("🔄 Processing data...")
        df = read_func(src_file)
        write_func(df, dest_file)
        print(f"✅ Success! Saved as: {dest_file}")
    except Exception as e:
        print(f"❌ Error: {e}")

def pdf_to_image():
    print("\n--- 🖼️ PDF to Image (PNG/JPG) ---")
    pdf_file = input("Enter path to PDF file: ").strip('"')
    format_type = input("Output format (png/jpeg): ").lower()
    
    output_folder = os.path.splitext(pdf_file)[0] + "_images"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    try:
        print("🔄 Extracting pages...")
        # Note: Requires Poppler installed on system
        images = convert_from_path(pdf_file)
        
        for i, image in enumerate(images):
            image.save(f"{output_folder}/page_{i+1}.{format_type}", format_type.upper())
            
        print(f"✅ Success! {len(images)} images saved in '{output_folder}'")
    except Exception as e:
        print(f"❌ Error: Is Poppler installed? ({e})")

def main_menu():
    while True:
        clear_screen()
        print("="*40)
        print("   SCRIPT SAVANT: DOCUMENT CONVERTER")
        print("="*40)
        print("1. 📄 Word -> PDF")
        print("2. 📝 PDF -> Word")
        print("3. 📊 Excel -> CSV")
        print("4. 📈 CSV -> Excel")
        print("5. 🖼️ PDF -> Images")
        print("0. 🚪 Exit")
        
        choice = input("\nEnter choice (0-5): ")
        
        if choice == '1': word_to_pdf()
        elif choice == '2': pdf_to_word()
        elif choice == '3': excel_csv_converter("to_csv")
        elif choice == '4': excel_csv_converter("to_xlsx")
        elif choice == '5': pdf_to_image()
        elif choice == '0': sys.exit()
        else: print("Invalid choice!")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()
