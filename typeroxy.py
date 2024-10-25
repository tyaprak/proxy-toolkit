import concurrent.futures
from proxy_checker import ProxyChecker
from datetime import datetime

DATE: datetime= datetime.now().strftime(format="%d-%m_%H-%M")

def worker(proxy) -> dict:
    checker = ProxyChecker()
    proxy=proxy.strip()
    res:dict = checker.check_proxy(proxy)
    if res:
        with open(rf"final_check-{DATE}.txt","a") as f:
            f.write(f"{proxy} - {res}\n")


def main() -> None:
    with open(r"C:\Users\HP\python\proxy-toolkit\proxies-2024_10_25_13_00_05.txt","r") as proxy_list:
        proxies = proxy_list.readlines()
        with concurrent.futures.ThreadPoolExecutor(max_workers=25) as executor:
            future_to_worker = {executor.submit(worker, proxy): proxy for proxy in proxies}
        for future in concurrent.futures.as_completed(future_to_worker):
            url = future_to_worker[future]
            try:
                data = future.result()
            except Exception as exc:
                print(f"Generated an exception: {exc}\n")

if __name__ == "__main__":
    main()