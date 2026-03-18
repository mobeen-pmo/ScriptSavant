import requests
from bs4 import BeautifulSoup
import re
import time

def clean_price(price_str):
    """Strips currency symbols and commas to return a clean float."""
    # Find all numbers and decimal points
    clean_str = re.sub(r'[^\d.]', '', price_str)
    try:
        return float(clean_str)
    except ValueError:
        return None

def check_price():
    print("\n" + "="*40)
    print("   SCRIPT SAVANT: UNIVERSAL PRICE TRACKER")
    print("="*40)
    
    url = input("\n🌐 Enter the product URL: ").strip()
    
    print("\n[Tip: Right-click the price on the webpage, select 'Inspect', and find the class name]")
    element_class = input("🏷️  Enter the HTML class name of the price (e.g., 'a-price-whole' or 'price-current'): ").strip()
    
    try:
        target_price = float(input("🎯 Enter your target price to drop below (e.g., 50.00): "))
    except ValueError:
        print("❌ Error: Please enter a valid number.")
        return

    # Use a standard browser User-Agent so websites don't immediately block us
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }

    print("\n🔄 Scraping the webpage... please wait.")
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code != 200:
            print(f"❌ Error: Website returned status code {response.status_code}. They might be blocking automated requests.")
            return
            
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Search for the element containing the price
        price_element = soup.find(class_=element_class)
        
        if not price_element:
            print(f"❌ Error: Could not find any element with the class '{element_class}'.")
            print("Try checking the website's HTML again.")
            return
            
        raw_price = price_element.get_text()
        current_price = clean_price(raw_price)
        
        if current_price is None:
            print(f"❌ Error: Found the element, but couldn't extract a valid number from: '{raw_price}'")
            return
            
        print(f"\n📊 Current Price found: ${current_price:.2f}")
        print(f"🎯 Your Target Price: ${target_price:.2f}")
        
        if current_price <= target_price:
            print("\n🎉🚨 PRICE DROP ALERT! 🚨🎉")
            print("The item has hit your target price! Go buy it now!")
        else:
            print("\n⏳ Not quite yet. The price is still too high.")
            
    except Exception as e:
        print(f"\n❌ ERROR: {e}")

if __name__ == "__main__":
    check_price()
