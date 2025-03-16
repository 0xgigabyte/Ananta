#!/usr/bin/env python3

import subprocess
import shutil
import sys
import os
from colorama import Fore, Style, init

init(autoreset=True)

# ASCII Banner
def banner():
    print(Fore.CYAN + """
╔══════════════════════════════════════════════╗
║        Cyber Offensive Toolkit               ║
║               BY 0xGigabyte                  ║
╚══════════════════════════════════════════════╝
""")

# Mindmap of Tools (ASCII)
def mindmap():
    print(Fore.GREEN + """
[1] Reconnaissance & OSINT
 ├─ subfinder (Subdomain Discovery)
 ├─ sublist3r (Subdomain Enumeration)
 ├─ assetfinder (Asset Discovery)
 ├─ amass (In-depth Enumeration)
 ├─ gau (URLs Gathering)
 └─ waybackurls (Archived URLs)

[2] Scanning
 ├─ httpx (HTTP Probe)
 ├─ nuclei (Vulnerability Scanner)
 ├─ naabu (Port Scanner)
 └─ dnsx (DNS Scanner)

[3] Exploitation & Privilege Escalation
 ├─ dalfox (XSS Exploitation)
 ├─ crlfuzz (CRLF Injection)
 └─ gobuster (Brute-force Directories)

[4] Network & Wireless Hacking
 ├─ naabu (Port Scanning)
 └─ dnsx (DNS Enumeration)

[5] Payloads & Backdoors
 ├─ gospider (Web Crawling)
 └─ ffuf (Web Fuzzing)

[6] Brute-Force & Cracking
 ├─ gobuster (Directory Brute-force)
 └─ crobat (Subdomain Brute-force)

[7] Red Team Automation
 ├─ notify (Notifications)
 └─ anew (New Asset Detection)
""")

# Tools with install commands and execution commands
tools = {
    "Reconnaissance & OSINT": {
        "subfinder": ("go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest", "subfinder -d {domain}"),
        "sublist3r": ("pip install sublist3r", "sublist3r -d {domain}"),
        "assetfinder": ("go install github.com/tomnomnom/assetfinder@latest", "assetfinder {domain}"),
        "amass": ("apt install amass -y", "amass enum -d {domain}"),
        "gau": ("go install github.com/lc/gau/v2/cmd/gau@latest", "gau {domain}"),
        "waybackurls": ("go install github.com/tomnomnom/waybackurls@latest", "waybackurls {domain}")
    },
    "Scanning": {
        "httpx": ("go install github.com/projectdiscovery/httpx/cmd/httpx@latest", "httpx -l {file}"),
        "nuclei": ("go install github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest", "nuclei -u {url}"),
        "naabu": ("go install github.com/projectdiscovery/naabu/v2/cmd/naabu@latest", "naabu -host {host}"),
        "dnsx": ("go install github.com/projectdiscovery/dnsx/cmd/dnsx@latest", "dnsx -d {domain}")
    },
    "Exploitation & Privilege Escalation": {
        "dalfox": ("go install github.com/hahwul/dalfox/v2@latest", "dalfox url {url}"),
        "crlfuzz": ("git clone https://github.com/dwisiswant0/crlfuzz.git && cd crlfuzz && go build && sudo cp crlfuzz /usr/local/bin/", "crlfuzz -u {url}"),
        "gobuster": ("apt install gobuster -y", "gobuster dir -u {url} -w /usr/share/wordlists/dirb/common.txt")
    },
    "Network & Wireless Hacking": {
        "naabu": ("go install github.com/projectdiscovery/naabu/v2/cmd/naabu@latest", "naabu -host {host}"),
        "dnsx": ("go install github.com/projectdiscovery/dnsx/cmd/dnsx@latest", "dnsx -d {domain}")
    },
    "Payloads & Backdoors": {
        "gospider": ("go install github.com/jaeles-project/gospider@latest", "gospider -s {url}"),
        "ffuf": ("go install github.com/ffuf/ffuf/v2@latest", 'ffuf -u "{url}/FUZZ" -w /usr/share/wordlists/dirb/common.txt')
    },
    "Brute-Force & Cracking": {
        "gobuster": ("apt install gobuster -y", 'gobuster dir -u {url} -w /usr/share/wordlists/dirb/common.txt'),
        "crobat": ("go install github.com/cgboal/sonarsearch/cmd/crobat@latest", 'crobat -s {domain}')
    },
    "Red Team Automation": {
        "notify": ("go install github.com/projectdiscovery/notify/cmd/notify@latest", 'notify'),
        "anew": ("go install github.com/tomnomnom/anew@latest", 'anew')
    }
}

def check_install(tool, cmd):
    if shutil.which(tool):
        print(f"{Fore.GREEN}[Installed]{Style.RESET_ALL} {tool}")
    else:
        print(f"{Fore.RED}[Not Installed]{Style.RESET_ALL} Installing {tool}")
        subprocess.run(cmd, shell=True)

def main():
    banner()
    mindmap()

    choice = input("\nDo you want to automatically INSTALL ALL tools? [yes/no]: ").lower()
    if choice == 'yes':
        for category in tools:
            for tool in tools[category]:
                check_install(tool, tools[category][tool][0])
    
    categories = list(tools.keys())
    while True:
        try:
            phase = int(input("\nSelect Attack Phase [1-7]: "))
            if 1 <= phase <= len(categories):
                break
            else:
                print(Fore.RED + f"Please select between 1 and {len(categories)}.")
        except ValueError:
            print(Fore.RED + f"Invalid input! Enter a number between 1 and {len(categories)}.")

    selected_category = categories[phase-1]
    tool_list = list(tools[selected_category].keys())

    for idx, tool in enumerate(tool_list, 1):
        status = Fore.GREEN+"Installed" if shutil.which(tool) else Fore.RED+"Not Installed"
        desc = tools[selected_category][tool][1].split()[:3]
        print(f"{Fore.CYAN}[{idx}] {tool:<15}{status:<15}{' '.join(desc)}")

    while True:
        try:
            tool_choice = int(input("Select Tool: "))
            if 1 <= tool_choice <= len(tool_list):
                break
            else:
                print(Fore.RED + f"Please select between 1 and {len(tool_list)}.")
        except ValueError:
            print(Fore.RED + f"Invalid input! Enter a number between 1 and {len(tool_list)}.")

    selected_tool = tool_list[tool_choice-1]
    cmd_format = tools[selected_category][selected_tool][1]

    params = {}
    if "{domain}" in cmd_format:
        params["domain"] = input("Enter domain [example.com]: ")
    if "{url}" in cmd_format:
        params["url"] = input("Enter URL [https://example.com]: ")
    if "{host}" in cmd_format:
        params["host"] = input("Enter host/IP [example.com or IP]: ")
    if "{file}" in cmd_format:
        params["file"] = input("Enter file path [urls.txt]: ")

    final_cmd = cmd_format.format(**params)
    
    print(Fore.YELLOW + f"\nExecuting: {final_cmd}\n")
    
    subprocess.run(final_cmd, shell=True)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\nOperation cancelled by user.")
