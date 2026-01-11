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

```bash
git clone https://github.com/imuday984/Ransom_Final.git
cd Ransom_Final

2. Install Dependencies
pip install -r requirements.txt

3. Start the Server
python server.py

4. Run the Agent
python agent3.py