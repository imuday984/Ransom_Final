# Ransom-Sentry: Ransomware Readiness Auditor 🛡️

**Author:** <YOUR NAME HERE>  
**Project Type:** Defensive Cybersecurity / Breach & Attack Simulation (BAS)

---

## ⚠️ Disclaimer

**This software is for EDUCATIONAL and DEFENSIVE testing purposes only.**  
It is designed to simulate ransomware-like behavior on dummy files to test antivirus/EDR response and system resilience.

❗ This tool:
- Does NOT contain real malware
- Does NOT spread
- Does NOT attack real data
- Works only inside a controlled test directory

The author is not responsible for misuse of this software.

---

## 📖 Overview

**Ransom-Sentry** is a *Ransomware Readiness Auditor* — a Breach and Attack Simulation (BAS) tool that helps users verify whether their endpoint protection (like Windows Defender or EDR solutions) can detect and stop ransomware-like behavior.

The tool safely simulates:
- Rapid file modification
- Encryption of dummy files
- Behavior-based detection triggers

It then reports whether the security software responded appropriately.

---

## 🧩 Architecture

The system follows a simple client-server model:

1. **Agent**
   - Runs locally on the test PC.
   - Creates dummy files in a test directory.
   - Encrypts them safely using AES (Fernet).
   - Monitors if antivirus blocks the behavior.
   - Rolls back all changes after the test.

2. **Server (Dashboard)**
   - Flask-based backend.
   - Displays live simulation logs.
   - Shows whether the system is protected or vulnerable.

---

## 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| Language | Python 3.13 |
| Encryption | cryptography (Fernet / AES) |
| Backend | Flask |
| Frontend | HTML / Console UI |
| Packaging | PyInstaller (optional) |

---

## 🚀 How to Run

### 1. Clone the Repository


    git clone https://github.com/imuday984/Ransom_Final.git
    cd Ransom_Final

    2. Install Dependencies
    pip install -r requirements.txt

    3. Start the Server
    python server.py

    4. Run the Agent
    python agent3.py
##  About
# 🛡️ Ransomware Readiness Auditor

![Type](https://img.shields.io/badge/Type-Simulation-blue) ![Language](https://img.shields.io/badge/Python-3.x-green) ![Safety](https://img.shields.io/badge/Safety-Sandboxed-orange)

## ⚙️ How It Works
This tool functions as a harmless "fire drill" for your computer security. It follows a strictly controlled 3-step lifecycle:

1.  **Preparation:**  
    The tool automatically creates a **"Safety Sandbox"** folder named `Ransom_Test_Zone` and populates it with dummy text files to ensure no real user data is ever touched.
2.  **Simulation (The Agent):**  
    The "Agent" program scans this specific folder and mimics a real attack by rapidly **encrypting (locking)** every file using military-grade **AES-256** encryption.
3.  **Reporting (The Server):**  
    While the simulation runs, the Agent sends live telemetry logs to a **Command & Control Server** (a local web dashboard), allowing you to visualize the attack progress in real-time.

---

## 🎯 Why Did I Build This?
Standard Antivirus software typically relies on **Signatures** (checking files against a known database of viruses). This tool is designed to test **Heuristics** (behavioral analysis).

It tests how your system reacts to an unknown program modifying files rapidly:

*   ✅ **The System is Safe:** If Windows Defender/Antivirus detects the rapid file modification and blocks/kills the process.
*   ⚠️ **The System is Vulnerable:** If the program runs to completion and successfully encrypts the files without interruption.

---

## 🛠️ Key Technologies Used
*   **Python:** Used for the core logic of the malware simulation.
*   **Flask:** Powers the web-based reporting dashboard (C2 Server).
*   **Cryptography Module:** Implements real, functioning AES file encryption standards.
*   **Client-Server API:** Establishes the communication verification between the Agent (Malware) and the Server.

---

## 🔒 Is It Safe?
**100% Yes.**

*   **Sandboxed Environment:** The code contains hardcoded logic that restricts it to **ONLY** operate inside the `Ransom_Test_Zone` directory.
*   **No Risk to Data:** The tool physically cannot verify, read, encrypt, or delete any other file on the user's computer outside of this specific test folder.
