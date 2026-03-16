import os
import pandas as pd

def generate_report(file_path):
    print("\n" + "="*40)
    print("   SCRIPT SAVANT: AUTOMATED DATA ANALYZER")
    print("="*40)
    
    if not os.path.exists(file_path) or not file_path.endswith('.csv'):
        print("❌ Error: Valid CSV file not found!")
        return

    try:
        print(f"\n🔄 Loading {os.path.basename(file_path)}... please wait.")
        df = pd.read_csv(file_path)
        
        # Create output report path
        report_path = file_path.replace(".csv", "_analysis_report.txt")
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"📊 DATA ANALYSIS REPORT FOR: {os.path.basename(file_path)}\n")
            f.write("="*50 + "\n\n")
            
            # 1. Basic Overview
            f.write("📋 1. OVERVIEW\n")
            f.write(f"Total Rows: {df.shape[0]}\n")
            f.write(f"Total Columns: {df.shape[1]}\n")
            f.write(f"Duplicate Rows: {df.duplicated().sum()}\n\n")
            
            # 2. Missing Values
            f.write("⚠️ 2. MISSING VALUES\n")
            missing_data = df.isnull().sum()
            if missing_data.sum() == 0:
                f.write("No missing values found! The dataset is clean.\n\n")
            else:
                f.write(missing_data[missing_data > 0].to_string() + "\n\n")
            
            # 3. Data Types
            f.write("🔠 3. DATA TYPES\n")
            f.write(df.dtypes.to_string() + "\n\n")
            
            # 4. Statistical Summary (Numerical columns only)
            f.write("📈 4. STATISTICAL SUMMARY (Numerical Features)\n")
            f.write(df.describe().T.to_string() + "\n")
            
        print(f"\n✅ SUCCESS! Analysis complete.")
        print(f"📄 Report saved securely at: {report_path}")

    except Exception as e:
        print(f"\n❌ ERROR: Could not analyze the dataset. Details: {e}")

if __name__ == "__main__":
    target_file = input("\n📁 Enter the path of the CSV file to analyze: ").strip('"')
    generate_report(target_file)
