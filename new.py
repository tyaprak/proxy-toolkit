import concurrent.futures
from datetime import datetime
from proxy_checker import ProxyChecker
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

DATE: str = datetime.now().strftime("%d-%m_%H-%M")
OUTPUT_FILE = rf"final_check-{DATE}.txt"
MAX_WORKERS = 200
PROXY_FILE = r"proxies-2024_11_19_00_17.txt"


def check_proxy(proxy: str) -> dict | None:
    """
    Checks a single proxy and returns its details if valid, otherwise None.

    Args:
        proxy: The proxy string to check.

    Returns:
        A dictionary of proxy details if valid, otherwise None.
    """
    checker = ProxyChecker()
    try:
        return checker.check_proxy(proxy)
    except Exception as e:
        logging.error(f"Error checking proxy {proxy}: {e}")
        return None


def write_valid_proxy(proxy: str, details: dict) -> None:
    """
    Writes a valid proxy and its details to the output file.

    Args:
        proxy: The valid proxy string.
        details: The details of the valid proxy.
    """
    with open(OUTPUT_FILE, "a") as f:
        f.write(f"{proxy} - {details}\n")


def worker(proxy: str) -> str | None:
    """
    Worker function that checks a proxy and writes it to the output file if valid.

    Args:
        proxy: The proxy to check.
    
    Returns:
       The result of future, if proxy is valid, proxy string will return, otherwise None.
    """
    proxy = proxy.strip()
    details = check_proxy(proxy)
    if details:
        write_valid_proxy(proxy, details)
        return proxy
    return None


def main() -> None:
    """
    Main function that reads proxies, checks them concurrently, and outputs the valid ones.
    """
    try:
        with open(PROXY_FILE, "r") as proxy_list:
            proxies = [line.strip() for line in proxy_list]
    except FileNotFoundError:
        logging.error(f"File {PROXY_FILE} not found.")
        return

    sorted_proxies = sorted(proxies)

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_proxy = {executor.submit(worker, proxy): proxy for proxy in sorted_proxies}
        for future in concurrent.futures.as_completed(future_to_proxy):
            proxy = future_to_proxy[future]
            try:
                result = future.result()
                if result:
                    logging.info(f"Valid proxy found: {result}")
            except Exception as e:
                logging.error(f"Proxy {proxy} generated an exception: {e}")


if __name__ == "__main__":
    main()
