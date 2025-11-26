**🛡️ Python Nmap Port Scanner**

This is a simple and beginner-friendly Python port scanner that uses the nmap library.

It scans ports 1–1024, checks their state, and identifies the service running on each port.

Useful for learning cybersecurity, network scanning, and ethical hacking basics.


**🔧 Requirements**

Install Python dependencies:

pip install python-nmap


**Install Nmap (required for the tool to run):**

Download from: https://nmap.org/download.html


**Make sure nmap works:**

nmap --version


**▶️ How to Run**

python scanner.py


Enter the target IP address when asked:

==== Advanced Python Nmap Scanner ====

Enter IP to scan: 192.168.1.1


**📌 Features**

Scans ports 1–1024

Uses -sV to detect service versions

Shows:

   Host status

   Open/closed ports

   Service names

  Product (software) running


**📂 Project Structure**

scanner.py

requirements.txt

README.md


**📘 Example Output**

Host: 192.168.1.1

State: up

[+] Port 22 (ssh) is open — Service: OpenSSH

[+] Port 80 (http) is open — Service: Apache


**⚠️ Disclaimer**

This tool is for educational and ethical use only.

Scan only systems you own or have permission for.
