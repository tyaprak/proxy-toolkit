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
    urls+=["https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies_anonymous/all.txt"]
    urls += [
    "https://api.proxyscrape.com/?request=getproxies&proxytype=https&timeout=10000&country=all&ssl=all&anonymity=all",
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",
    "https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/cnfree.txt",
    "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt",
    "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt"
]
    urls += [
        "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4",
        "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all",
        "https://api.openproxylist.xyz/socks4.txt",
        "https://proxyspace.pro/socks4.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks4.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
        "https://proxyspace.pro/socks4.txt",
        "https://www.proxy-list.download/api/v1/get?type=socks4",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
        "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt",
        "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt",
        "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/socks4.txt",
        "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks4.txt",
        "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks4.txt",
        "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks4.txt",
        "https://raw.githubusercontent.com/prxchk/proxy-list/main/socks4.txt",
        "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks4.txt",
        "https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt",
    ]

    urls += [
        "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS5.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
        "https://api.openproxylist.xyz/socks5.txt",
        "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5",
        "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5",
        "https://proxyspace.pro/socks5.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
        "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
        "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt",
        "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/socks5.txt",
        "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks5.txt",
        "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks5.txt",
        "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt",
        "https://raw.githubusercontent.com/prxchk/proxy-list/main/socks5.txt",
        "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks5.txt",
        "https://spys.me/socks.txt",
        "https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt"
    ]
    regex_pattern = r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?):\d{1,5}\b"  # Regex for IP:PORT
    proxies = []
    for url in urls:
        matches = extract_regex_pattern(url, regex_pattern)
        if matches:
            for match in matches:
                proxies.append(match)
        else:
            print("No matches found.")
    return list(set(proxies))

def main():
    ll = proxy_collector()
    l = len(ll)
    n = datetime.now().strftime("%Y_%m_%d_%H_%M")
    with Bar('Processing', max=l) as bar:
        for proxy in ll:
            with open(f"proxies-{n}.txt", "a") as file:
                file.write(f"{proxy}\n")
            bar.next()

if __name__ == "__main__":
    main()