import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from colorama import init, Fore, Style

# Initialize colorama for Windows support
init(autoreset=True)

def is_valid_url(url):
    """Checks if the URL has a valid structure."""
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def skim_website():
    print(f"\n{Fore.CYAN}{'='*50}")
    print(f"{Fore.CYAN}   SCRIPT SAVANT: WEB SKIMMER & LINK AUDITOR")
    print(f"{Fore.CYAN}{'='*50}\n")
    
    base_url = input(f"{Fore.YELLOW}🌐 Enter the URL to skim (e.g., https://github.com): {Style.RESET_ALL}").strip()
    
    if not is_valid_url(base_url):
        print(f"{Fore.RED}❌ Error: Invalid URL format. Please include http:// or https://")
        return

    check_broken = input(f"{Fore.YELLOW}🔍 Do you want to check for broken links? This takes longer. (y/n): {Style.RESET_ALL}").lower() == 'y'

    print(f"\n{Fore.BLUE}🔄 Skimming {base_url}... please wait.{Style.RESET_ALL}")
    
    try:
        # Custom headers to prevent basic blocks
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(base_url, headers=headers, timeout=10)
        
        if response.status_code != 200:
            print(f"{Fore.RED}❌ Error: Website returned status {response.status_code}{Style.RESET_ALL}")
            return
            
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract all anchor tags
        all_links = set()
        for a_tag in soup.find_all("a"):
            href = a_tag.attrs.get("href")
            if href == "" or href is None:
                continue
                
            # Resolve relative URLs to absolute URLs
            full_url = urljoin(base_url, href)
            
            # Keep only HTTP/HTTPS links (ignore mailto:, javascript:, etc.)
            if is_valid_url(full_url):
                all_links.add(full_url)
                
        print(f"\n{Fore.GREEN}✅ Found {len(all_links)} unique links on the page.{Style.RESET_ALL}\n")
        
        if check_broken:
            print(f"{Fore.BLUE}🚦 Auditing links for 404 errors...{Style.RESET_ALL}")
            broken_links = []
            working_links = 0
            
            for i, link in enumerate(all_links, 1):
                try:
                    # Use a HEAD request instead of GET for speed
                    res = requests.head(link, headers=headers, timeout=5, allow_redirects=True)
                    if res.status_code >= 400:
                        print(f"{Fore.RED}[{i}] BROKEN ({res.status_code}): {link}{Style.RESET_ALL}")
                        broken_links.append((link, res.status_code))
                    else:
                        print(f"{Fore.GREEN}[{i}] OK: {link}{Style.RESET_ALL}")
                        working_links += 1
                except requests.RequestException:
                    print(f"{Fore.RED}[{i}] FAILED (Timeout/Connection): {link}{Style.RESET_ALL}")
                    broken_links.append((link, "Connection Error"))
            
            print(f"\n{Fore.CYAN}--- AUDIT SUMMARY ---{Style.RESET_ALL}")
            print(f"Working Links: {working_links}")
            print(f"Broken/Failed Links: {len(broken_links)}")
            
        else:
            # Just print the links if they didn't want to audit
            for i, link in enumerate(all_links, 1):
                print(f"[{i}] {link}")
                
    except Exception as e:
        print(f"\n{Fore.RED}❌ ERROR: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    skim_website()
