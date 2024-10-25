# 🌊 Persian Gulf Forever - Multi-Country DNS Generator 🌊
# =====================================================

import random
import socket
from colorama import Fore, Style, init

init(autoreset=True)

def display_persian_gulf_banner():
    print(Fore.CYAN + "\n🌊 Persian Gulf Forever 🌊" + Style.RESET_ALL)
    print("=" * 40 + "\n")

patterns_ipv4 = {
    "Global": ["8.8.{0}.{1}", "1.1.{0}.{1}"],
    "Europe": ["80.80.{0}.{1}", "5.135.{0}.{1}"],
    "Asia": ["203.0.{0}.{1}", "210.48.{0}.{1}"],
    "America": ["4.2.2.{0}", "74.125.{0}.{1}"]
}
patterns_ipv6 = {
    "Global": ["2001:4860:{0}:{1}::", "2400:cb00:{0}:{1}:{2}::1"],
    "Europe": ["2a02:6b8:{0}:{1}::{2}", "2a00:1450:{0}:{1}::"],
    "Asia": ["2404:6800:{0}:{1}::", "2400:cb00:{0}:{1}:{2}::1"],
    "America": ["2607:f8b0:{0}:{1}::{2}", "2800:3f0:{0}:{1}:{2}::"]
}

#  ipv4
def generate_random_ipv4(region):
    if region in patterns_ipv4:
        pattern = random.choice(patterns_ipv4[region])
        primary_dns = pattern.format(random.randint(0, 255), random.randint(0, 255))
        return primary_dns
    else:
        return "Invalid region"

# ipv6
def generate_random_ipv6(region):
    if region in patterns_ipv6:
        pattern = random.choice(patterns_ipv6[region])
        primary_dns = pattern.format(
            hex(random.randint(0, 65535))[2:], 
            hex(random.randint(0, 65535))[2:], 
            hex(random.randint(0, 65535))[2:]
        )
        return primary_dns
    else:
        return "Invalid region"

def test_dns_connection(dns):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(2)
       
        result = sock.connect_ex((dns, 53))
        if result == 0:
            print(Fore.GREEN + f"✅ Connection to DNS {dns} successful on port 53." + Style.RESET_ALL)
        else:
            print(Fore.RED + f"❌ Connection to DNS {dns} failed on port 53." + Style.RESET_ALL)
        sock.close()
    except Exception as e:
        print(Fore.RED + f"Error during connection test: {e}" + Style.RESET_ALL)

def dns_panel():
    display_persian_gulf_banner()
    print("🌐 | DNS Generation and Connection Testing Panel\n")
    while True:
        print("Choose an option:\n1. Generate random IPv4 DNS\n2. Generate random IPv6 DNS\n3. Exit")
        choice = input("Your choice: ")
        
        if choice == "1":
            region = input("Enter region (Global, Europe, Asia, America): ")
            primary = generate_random_ipv4(region)
            print(Fore.WHITE + f"🔄 Generated IPv4 DNS (Primary): {primary}")
            test_dns_connection(primary)
            print()
        
        elif choice == "2":
            region = input("Enter region (Global, Europe, Asia, America): ")
            primary = generate_random_ipv6(region)
            print(Fore.WHITE + f"🔄 Generated IPv6 DNS (Primary): {primary}")
            test_dns_connection(primary)
            print()
        
        elif choice == "3":
            print(Fore.GREEN + "Exiting the panel." + Style.RESET_ALL)
            break
        
        else:
            print(Fore.RED + "Invalid choice, please try again." + Style.RESET_ALL)

# Run the panel
dns_panel()