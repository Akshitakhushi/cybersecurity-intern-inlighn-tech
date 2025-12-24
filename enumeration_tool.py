import dns.resolver

domain = input("Enter domain name: ")

try:
    result = dns.resolver.resolve(domain, 'A')
    for ip in result:
        print("IP Address:", ip)
except Exception as e:
    print("Error:", e)
