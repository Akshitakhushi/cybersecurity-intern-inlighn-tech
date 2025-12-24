import requests
import threading
domain = "youtube.com"
with open('subdomain.txt') as file:
    subdomain = file.read().splitlines()

discivered_subdomain = []
lock = threading.Lock()

def check_subdomain(subdomain):
    url = f'http://{subdomain}.{domain}'
    try:
        requests.get(url, timeout=3)
    except requests.ConnectionError:
        pass
    else:
        print("[+]Discovered Subdomains:",url)
        with lock:
            discivered_subdomain.append(url)
threads = []
for subdomain in subdomain :
    thread = threading.Thread(target=check_subdomain, args=(subdomain,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
with open("discovered_subdomain.txt",'w') as f:
    for subdomain in discivered_subdomain:
        print(subdomain, file=f)