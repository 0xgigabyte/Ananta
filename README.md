# ANANTA 🚀
🔥 Overview
### The Cyber Offensive Toolkit is a Python-based interactive framework designed for offensive cybersecurity operations. It integrates multiple tools across various attack phases, including reconnaissance, scanning, exploitation, brute-forcing, and red team automation. This toolkit simplifies the execution of complex security tasks by automating tool installation, parameter handling, and execution.

🛠️ Use Cases
This toolkit is ideal for:

Reconnaissance & OSINT: Subdomain discovery, asset enumeration, and archived URL gathering.

Scanning: HTTP probing, DNS enumeration, and port scanning.

Exploitation & Privilege Escalation: XSS exploitation, CRLF injection detection, and directory brute-forcing.

Network & Wireless Hacking: Port scanning and DNS enumeration.

Payloads & Backdoors: Web crawling and fuzzing.

Brute-Force & Cracking: Subdomain brute-forcing and directory brute-forcing.

Red Team Automation: Notifications and asset tracking.

📂 Tool Structure
Here’s the ASCII mindmap of the toolkit’s structure:
Ananta
├── [1] Reconnaissance & OSINT
│   ├─ subfinder (Subdomain Discovery)
│   ├─ sublist3r (Subdomain Enumeration)
│   ├─ assetfinder (Asset Discovery)
│   ├─ amass (In-depth Enumeration)
│   ├─ gau (URLs Gathering)
│   └─ waybackurls (Archived URLs)
├── [2] Scanning
│   ├─ httpx (HTTP Probe)
│   ├─ nuclei (Vulnerability Scanner)
│   ├─ naabu (Port Scanner)
│   └─ dnsx (DNS Scanner)
├── [3] Exploitation & Privilege Escalation
│   ├─ dalfox (XSS Exploitation)
│   ├─ crlfuzz (CRLF Injection Detection)
│   └─ gobuster (Directory Brute-force)
├── [4] Network & Wireless Hacking
│   ├─ naabu (Port Scanning)
│   └─ dnsx (DNS Enumeration)
├── [5] Payloads & Backdoors
│   ├─ gospider (Web Crawling)
│   └─ ffuf (Web Fuzzing)
├── [6] Brute-Force & Cracking
│   ├─ gobuster (Directory Brute-force)
│   └─ crobat (Subdomain Brute-force)
└── [7] Red Team Automation
    ├─ notify (Notifications)
    └─ anew (New Asset Detection)
    
#### ⚙️ Features
✅ Fully functional execution of integrated tools
✅ Automated dependency management
✅ Interactive user guidance with clear prompts
✅ Menu-driven navigation for attack phases and tools
✅ ASCII art enhancements for better visualization
✅ Real-time status indication for installed tools
✅ Error handling for invalid inputs

#### 🚀 Installation
Prerequisites:
Ensure you have the following installed:

```Python 3.x  

Golang
Git 
```
Install Golang:
bash
sudo apt update && sudo apt install golang-go -y
Install Python3 and pip:
bash
sudo apt update && sudo apt install python3 python3-pip -y
Install Git:
bash
sudo apt install git -y
Clone the Repository:
bash
git clone https://github.com/yourusername/cyber-offensive-toolkit.git
cd cyber-offensive-toolkit 
Run the Script:
Execute the script using Python:

bash
python3 cyber_offensive_toolkit.py
🌟 How to Use
Select Installation Mode: When prompted, choose whether to install all tools automatically (yes) or proceed directly (no).

View Attack Phases: Navigate through the ASCII mindmap displaying categorized tools.

Select Attack Phase: Choose from reconnaissance, scanning, exploitation, etc.

Choose Tool: Pick a specific tool within the selected category. Installed tools are marked green; missing ones are marked red.

Enter Parameters: Provide required inputs such as domain names, URLs, file paths, etc., guided by clear examples.

Execute Tool: The toolkit runs the selected tool with your parameters and displays real-time output.

📦 Tools Included
Reconnaissance & OSINT:
```subfinder: Subdomain discovery
sublist3r: Subdomain enumeration
assetfinder: Asset discovery
amass: In-depth enumeration
gau: Gather URLs
waybackurls: Archived URLs
```
Scanning:
```httpx: HTTP probing
nuclei: Vulnerability scanning
naabu: Port scanning
dnsx: DNS enumeration
```
Exploitation & Privilege Escalation:
```dalfox: XSS exploitation
crlfuzz: CRLF injection detection
gobuster: Directory brute-forcing
```
Network & Wireless Hacking:
```
naabu: Port scanning
dnsx: DNS enumeration
Payloads & Backdoors:
gospider: Web crawling
ffuf: Web fuzzing
Brute-force & Cracking:
gobuster: Directory brute-forcing
crobat: Subdomain brute-forcing
Red Team Automation:
notify: Notifications
anew: Asset tracking
```
🛡️ Disclaimer
This tool is intended for ethical hacking and cybersecurity research purposes only. Unauthorized use of this toolkit against systems without explicit permission is illegal and unethical.

✨ Contributing
Feel free to fork this repository and submit pull requests for improvements or additional features! Contributions are always welcome.
