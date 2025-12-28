# meldi-integrity-checker-
i can use ai. ai make it easy. hehe


# MELDI 🛡️  
**Malware Early Light Detection Integrity Tool**

A simple yet powerful **File Integrity Monitoring (FIM)** tool built in Python using SHA-256 hashing to detect file modifications, additions, and deletions.

Perfect cybersecurity educational project for learning:
- Cryptographic hashing
- File system traversal
- Integrity checking
- Real-world security concepts

**Created by: shyclone 🌀**  
*Cyber Security Student Project – December 2025*

## Features ✨
- Recursive scanning of folders and subfolders
- SHA-256 hashing for strong tamper detection
- Automatic baseline creation (unique JSON file per folder)
- Clear detection of **Modified ✏️**, **Added 🆕**, and **Deleted 🗑️** files
- Beautiful colored terminal interface with ASCII banner
- Interactive menu – easy to use

## Screenshots
*(Run the tool to see the epic banner and colored output in action!)*

## How to Run

### Requirements
- Python 3.6 or higher
- Only one dependency: `colorama`

### Installation & Run
1. Clone or download this repository
2. Open terminal in the project folder
3. Install the required package:
   ```bash
   pip install colorama


Usage

Select 1 → Create New Baseline
→ Enter full path to the folder you want to monitor
MELDI creates a baseline (e.g., MyFolder_baseline.json)
Make changes to files in that folder
Select 2 → Check for Changes
→ Enter the same folder path → View detailed tampering report

Example Output
text🛡️  REAL-TIME FILE TAMPERING DETECTION SYSTEM 🛡️

CHANGES DETECTED:

MODIFIED files:
   ✏️  notes.txt

ADDED files:
   🆕 secret_document.pdf

DELETED files:
   🗑️  temp_backup.zip
Project Structure
textMELDI/
├── meldi.py          # Main source code
├── README.md         # This file
└── (baseline files will be created here when running)
Why MELDI?
Inspired by professional tools like Tripwire, OSSEC, and AIDE.
This project demonstrates core cybersecurity principles in a simple, readable way.
"Early detection is the best defense." – shyclone 🌀
License
Free for educational use, modification, and sharing.
Feel free to fork, improve, and learn!

Thank you for checking out MELDI!
Stay curious. Stay secure. 🛡️🔥
— shyclone
