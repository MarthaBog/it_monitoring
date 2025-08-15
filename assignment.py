import sys 
import time 
import requests 

def check_url(url: str, timeout: float = 10.0): # 10 sec should be more than enough for server to wait for response from site
    start = time.perf_counter()
    try:
        response = requests.get(url, timeout=timeout)
        elapsed_time_ms = (time.perf_counter() - start) * 1000.0 
        code = response.status_code
        result = "OK" if code == 200 else "NOK"
        return code, result, elapsed_time_ms
    except requests.RequestException: 
        elapsed_time_ms = (time.perf_counter() - start) * 1000.0
        return 0, "NOK", elapsed_time_ms

if len(sys.argv) != 2:
    print("Website is not specified! Usage: python assignment.py https://www.delfi.ee/")
    sys.exit(1)

url = sys.argv[1] 
code, result, ms = check_url(url)
print(f"code={code} result={result} time_ms={ms:.2f}")

sys.exit(0 if result == "OK" else 1) 
