# Ransom-Sentry: Ransomware Readiness Auditor 🛡️

### ⚠️ Disclaimer
**This software is for EDUCATIONAL and DEFENSIVE testing purposes only.**  
It is designed to simulate a ransomware attack pattern to test Antivirus/EDR response and system resilience. The author is not responsible for any misuse of this code.

---

### 📖 Overview
Ransom-Sentry is a **Breach and Attack Simulation (BAS)** tool. It consists of a Client-Server architecture:
1.  **The Agent:** Simulates file encryption behavior (using safe AES encryption) on dummy files.
2.  **The Server:** A Flask-based C2 (Command & Control) dashboard that monitors the "attack" in real-time.

### 🛠️ Tech Stack
- **Language:** Python 3.13
- **Encryption:** Cryptography (Fernet/AES)
- **Backend:** Flask
- **Compilation:** PyInstaller (for Agent EXE generation)

### 🚀 How to Run

1. **Clone the Repo**
   ```bash
   git clone https://github.com/imuday984/Ransom_Final.git
   cd Ransom_Final