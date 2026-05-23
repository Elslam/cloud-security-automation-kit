"""
Cloud Security Automation Script: Log & Extension Auditor
Description: Automated script to parse flat lists for malicious extensions 
             and unauthorized applications on a local network node.
"""

# Test Data 1: Simulated file downloads on a local endpoint
downloaded_files = ["report.pdf", "backup.zip", "installer.exe", "notes.txt", "script.sh"]

# List Comprehension explicitly checking for dangerous executable/script extensions
#dangerous_files = [file.lower().strip() for file in downloaded_files if ".sh" in file.lower().strip() or ".exe" in file.lower().strip()]
#While I used .lower() and .strip() on the first file on our list comprehension example for the cleanness, by us using .lower() and .strip() 3 times is making our code run slower. Heres a shorter way...
dangerous_files = [file.lower().strip() for file in downloaded_files if file.lower().strip().endswith((".sh", ".exe"))]

print("--- SECURITY AUDIT: FILE EXTENSIONS ---")
print(f"Flagged Files for Inspection: {dangerous_files}\n")


# Test Data 2: Active application processes on a LAN node
running_apps = ["Python", "Slack", "Torrent-Downloader", "Chrome", "Malicious-Scanner", "VSCode"]

# Extracting policy violations using chained string matching conditions
policy_violations = [app.lower().strip() for app in running_apps if "downloader" in app.lower().strip() or "scanner" in app.lower().strip()]
#The reason I didn't use .endswith() here because in our first example it is a file extension it has to end with it. However in our second example an uninvited node (hacker) can put these keywords in the middle or in the beginning thats exactly why I used in to be flawless.

print("--- SECURITY AUDIT: RUNNING APPLICATIONS ---")
print(f"Unauthorized Software Detected: {policy_violations}")
