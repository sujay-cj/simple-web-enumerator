🌐 Simple Web Enumerator

A beginner-friendly Python tool to discover hidden directories on a web server using a wordlist. Designed for learning, CTFs, and basic web enumeration.

🚀 Features

🔍 Directory enumeration using a wordlist

🌐 Sends HTTP GET requests to each path

📊 Detects useful status codes:

200 → Page exists

301/302 → Redirects

403 → Exists but restricted

⏱️ Timeout support to prevent hanging

⚠️ Handles connection errors gracefully

🧠 Simple and easy-to-understand code

🛠️ Requirements

Python 3.x

requests library

Install dependency:

pip install requests
📂 Project Structure
simple-web-enumerator/
│
├── scanner.py
├── common.txt
└── README.md
▶️ Usage

Set your target URL in the script:

my_url = "http://target-ip"

Make sure your wordlist (common.txt) is in the same folder.

Run the script:

python scanner.py
📌 Example Output
Started scanning...

Found: http://10.10.230.135/admin
Status: 200 - OK (Page exists)

Found: http://10.10.230.135/backup
Status: 403 - Forbidden (Exists but no access)

Scan completed!
🧠 How It Works

Reads directory names from a wordlist

Combines them with the target URL

Sends HTTP requests

Filters responses based on status codes

Displays valid or interesting endpoints

⚠️ Disclaimer

This tool is intended for educational purposes only.
Use it only on systems you own or have permission to test.

🔮 Future Improvements

🚀 Add multithreading for faster scans

🎯 Support command-line arguments

🎨 Add colored output

💾 Save results to a file

👨‍💻 Author

Sujay CJ
Cybersecurity Enthusiast
