import sqlite3
import pandas as pd
import os
from tabulate import tabulate
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def connect_to_db():
    db_path = input("\n🗄️ Enter the path to your SQLite database (.db or .sqlite): ").strip('"')
    if not os.path.exists(db_path):
        print("❌ Error: Database file not found!")
        return None
    try:
        conn = sqlite3.connect(db_path)
        return conn, db_path
    except sqlite3.Error as e:
        print(f"❌ Connection Error: {e}")
        return None

def list_tables(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        if not tables:
            print("\n⚠️ This database has no tables.")
            return

        print("\n📋 AVAILABLE TABLES:")
        for i, table in enumerate(tables, 1):
            print(f"  {i}. {table[0]}")
            
    except sqlite3.Error as e:
        print(f"❌ Error reading tables: {e}")

def run_custom_query(conn, db_path):
    print("\n✍️  Type your SQL query below (type 'EXIT' to return to menu):")
    query = input("SQL> ").strip()
    
    if query.upper() == 'EXIT':
        return

    try:
        # We use pandas here because it handles fetching and formatting beautifully
        df = pd.read_sql_query(query, conn)
        
        if df.empty:
            print("\n✅ Query executed successfully, but returned 0 rows.")
            return
            
        print("\n📊 QUERY RESULTS:")
        # Print using tabulate for a beautiful terminal grid
        print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
        print(f"\nTotal rows: {len(df)}")
        
        # Bonus: Offer to export the results
        export = input("\n💾 Export these results to CSV? (y/n): ").lower()
        if export == 'y':
            base_name = os.path.splitext(os.path.basename(db_path))[0]
            out_file = f"{base_name}_query_export.csv"
            df.to_csv(out_file, index=False)
            print(f"✅ Saved successfully to {out_file}")

    except Exception as e:
        print(f"❌ Query Error: {e}")

def main_menu():
    print("\n" + "="*50)
    print("   SCRIPT SAVANT: SQL DATABASE MANAGER")
    print("="*50)
    
    connection_data = connect_to_db()
    if not connection_data:
        return
        
    conn, db_path = connection_data
    print(f"\n✅ Successfully connected to: {os.path.basename(db_path)}")

    while True:
        print("\n" + "-"*30)
        print("1. 📋 List all Tables")
        print("2. 🔍 Run a custom SQL Query (SELECT, UPDATE, etc.)")
        print("0. 🚪 Disconnect & Exit")
        
        choice = input("\nEnter choice (0-2): ")
        
        if choice == '1': 
            list_tables(conn)
        elif choice == '2': 
            run_custom_query(conn, db_path)
        elif choice == '0': 
            conn.close()
            print("👋 Disconnected. Goodbye!")
            break
        else: 
            print("Invalid choice!")

if __name__ == "__main__":
    main_menu()
