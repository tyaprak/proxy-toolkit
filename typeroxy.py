import concurrent.futures
from proxy_checker import ProxyChecker
from datetime import datetime

DATE: str = datetime.now().strftime("%d-%m_%H-%M")

def worker(proxy) -> None:
    checker = ProxyChecker()
    proxy=proxy.strip()
    res:dict = checker.check_proxy(proxy)
    if res:
        with open(rf"final_check-{DATE}.txt","a") as f:
            f.write(f"{proxy} - {res}\n")

def main() -> None:
    with open(r"proxies-2024_10_31_19_14.txt","r") as proxy_list:
        proxies = proxy_list.readlines()
        with concurrent.futures.ThreadPoolExecutor(max_workers=250) as executor:
            future_to_worker = {executor.submit(worker, proxy): proxy for proxy in proxies}
        for future in concurrent.futures.as_completed(future_to_worker):
            print(future.result())


if __name__ == "__main__":
    main()