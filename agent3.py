import os
import time
import requests
import sys
from cryptography.fernet import Fernet


SERVER_URL = "http://127.0.0.1:5000/report"

TARGET_FOLDER = os.path.join(os.getcwd(), "Ransom_Test_Zone") 

def send_alert(message, status):
    """Sends JSON data to the dashboard"""
    try:
        payload = {"message": message, "status": status}
        requests.post(SERVER_URL, json=payload, timeout=2)
    except Exception as e:
        print(f"Server Offline? {e}")

def setup_environment():
    """Creates the folder and dummy files"""
    send_alert("Initializing Test Environment...", "INFO")
    
    if not os.path.exists(TARGET_FOLDER):
        os.makedirs(TARGET_FOLDER)
    
    
    for i in range(1, 16):
        with open(os.path.join(TARGET_FOLDER, f"confidential_{i}.txt"), "w") as f:
            f.write("This is dummy data for a security simulation. " * 50)
    
    send_alert(f"Created 15 dummy files in {TARGET_FOLDER}", "INFO")

def simulate_encryption():
    """The Fake Attack"""
    send_alert("Testing Encryption Defense Mechanisms...", "WARNING")
    time.sleep(2) # Pause so you can see the dashboard update

    # 1. Generate Key
    key = Fernet.generate_key()
    cipher = Fernet(key)

    # 2. Find files
    files = [f for f in os.listdir(TARGET_FOLDER) if f.endswith(".txt")]
    
    if not files:
        send_alert("No files found to encrypt. Setup failed.", "SAFE")
        return

    encrypted_count = 0
    start_time = time.time()

    for file_name in files:
        file_path = os.path.join(TARGET_FOLDER, file_name)
        
        try:
            # Read
            with open(file_path, "rb") as f:
                original_data = f.read()
            
            # Encrypt
            encrypted_data = cipher.encrypt(original_data)
            
            # Write Back
            with open(file_path, "wb") as f:
                f.write(encrypted_data)
            
            # Rename (The visual scare)
            os.rename(file_path, file_path + ".LOCKED")
            encrypted_count += 1
            
            # Slow down slightly so the dashboard looks cool
            time.sleep(0.1) 

        except Exception as e:
            send_alert(f"Encryption blocked on {file_name}", "SAFE")

    duration = round(time.time() - start_time, 2)
    
    # Final Verdict
    if encrypted_count == len(files):
        msg = f"SIMULATION SUCCESS: {encrypted_count} files encrypted in {duration}s. System Vulnerable."
        send_alert(msg, "CRITICAL")
    else:
        send_alert("Simulation Partial/Failed. Antivirus may have intervened.", "SAFE")

    # SAVE THE KEY (Ethical Requirement)
    with open(os.path.join(TARGET_FOLDER, "decryption_key.key"), "wb") as k:
        k.write(key)
    send_alert("Decryption key saved locally. No data lost.", "INFO")

if __name__ == "__main__":
    print(f"--- RANSOMWARE READINESS AUDITOR ---")
    print(f"Target: {TARGET_FOLDER}")
    
    # User Consent
    consent = input("Type 'RUN' to start the simulation: ")
    if consent.strip().upper() == "RUN":
        setup_environment()
        simulate_encryption()
        print("\nAudit Complete.")
    else:
        print("Aborted.")