import re
import requests
from progress.bar import Bar
from datetime import datetime

def extract_regex_pattern(url, regex_pattern):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        content = response.text
        matches = re.findall(regex_pattern, content)
        return matches
    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from {url}: {e}")
        return []


def proxy_collector():
    urls = ["https://paste.fo/raw/44c68656d06d", "https://paste.fo/raw/b11fa14eb8ee", "https://paste.fo/raw/5c517a639347", "https://paste.fo/raw/c9532909bba9"]
    urls+=["https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt","https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt"]
    
    
    regex_pattern = r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?):\d{1,5}\b"  # Regex for IP:PORT
    proxies = []
    for url in urls:
        matches = extract_regex_pattern(url, regex_pattern)
        if matches:
            for match in matches:
                proxies.append(match)
        else:
            print("No matches found.")
    return proxies

if __name__ == "__main__":
    ll= proxy_collector()
    l = len(ll)
    n=datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    with Bar('Processing', max=l) as bar:
        for proxy in ll:
            with open(f"proxies-{n}.txt", "a") as file:
                file.write(f"{proxy}\n")
            bar.next()
