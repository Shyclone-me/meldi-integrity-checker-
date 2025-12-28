"""
MELDI - Malware Early Light Detection Integrity Tool
File Integrity Monitoring Tool using SHA-256 Hashes

Created by: shyclone 🌀
Date: December 2025

Features:
- Recursive folder scanning
- Automatic unique baseline files per folder
- Detects modified, added, and deleted files
- Beautiful colored interactive interface
"""

import os
import hashlib
import json
from colorama import init, Fore, Style

# Initialize colorama (Windows + auto color reset)
init(autoreset=True)


def compute_hash(file_path):
    """Calculate SHA-256 hash of a file in chunks for efficiency."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        print(Fore.RED + f"Error reading {file_path}: {e}")
        return None


def get_all_files(directory):
    """Return list of relative paths for all files in directory (recursive)."""
    all_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, directory)
            all_files.append(rel_path)
    return all_files


def generate_baseline(directory):
    """Create and save a baseline JSON file with hashes for all files."""
    print(Fore.CYAN + f"\nScanning folder: {directory}")
    
    folder_name = os.path.basename(os.path.normpath(directory))
    baseline_file = f"{folder_name}_baseline.json"
    
    print(Fore.YELLOW + f"Saving baseline as: {baseline_file}\n")
    
    file_list = get_all_files(directory)
    
    if not file_list:
        print(Fore.RED + "No files found in the folder!")
        return
    
    hashes = {}
    for rel_path in file_list:
        full_path = os.path.join(directory, rel_path)
        file_hash = compute_hash(full_path)
        if file_hash:
            hashes[rel_path] = file_hash
            print(Fore.GREEN + f"✓ Hashed: {rel_path}")
        else:
            print(Fore.RED + f"✗ Skipped (error): {rel_path}")
    
    with open(baseline_file, "w") as f:
        json.dump(hashes, f, indent=4)
    
    print(Fore.GREEN + Style.BRIGHT +
          f"\nBaseline complete! Saved {len(hashes)} file hashes to {baseline_file}")
    print(Fore.CYAN + "Use this baseline when verifying this folder later.\n")


def verify_integrity(directory):
    """Verify current folder state against its baseline and report changes."""
    print(Fore.CYAN + f"\nVerifying folder: {directory}\n")
    
    folder_name = os.path.basename(os.path.normpath(directory))
    baseline_file = f"{folder_name}_baseline.json"
    
    print(Fore.YELLOW + f"Looking for baseline: {baseline_file}\n")
    
    # Load baseline
    try:
        with open(baseline_file, "r") as f:
            old_hashes = json.load(f)
        print(Fore.CYAN + f"Loaded baseline with {len(old_hashes)} files.\n")
    except FileNotFoundError:
        print(Fore.RED + Style.BRIGHT + f"Error: {baseline_file} not found!")
        print(Fore.YELLOW + "Tip: Run 'Create New Baseline' for this folder first.\n")
        return
    except Exception as e:
        print(Fore.RED + f"Error reading baseline: {e}")
        return
    
    # Compute current hashes
    current_hashes = {}
    current_files = get_all_files(directory)
    
    for rel_path in current_files:
        full_path = os.path.join(directory, rel_path)
        file_hash = compute_hash(full_path)
        if file_hash:
            current_hashes[rel_path] = file_hash
    
    print(Fore.CYAN + f"Currently found {len(current_hashes)} files.\n")
    
    # Detect changes
    modified = []
    added = []
    deleted = []
    
    for rel_path, old_hash in old_hashes.items():
        if rel_path not in current_hashes:
            deleted.append(rel_path)
        elif current_hashes[rel_path] != old_hash:
            modified.append(rel_path)
    
    for rel_path in current_hashes:
        if rel_path not in old_hashes:
            added.append(rel_path)
    
    # Report results
    if not modified and not added and not deleted:
        print(Fore.GREEN + Style.BRIGHT + "🎉 GOOD NEWS: No changes detected! All files are intact.\n")
    else:
        print(Fore.RED + Style.BRIGHT + "⚠️  CHANGES DETECTED:\n")
        
        if modified:
            print(Fore.YELLOW + "MODIFIED files:")
            for m in modified:
                print(Fore.YELLOW + f"   ✏️  {m}")
            print()
        
        if added:
            print(Fore.GREEN + "ADDED files:")
            for a in added:
                print(Fore.GREEN + f"   🆕 {a}")
            print()
        
        if deleted:
            print(Fore.RED + "DELETED files:")
            for d in deleted:
                print(Fore.RED + f"   🗑️  {d}")
            print()


if __name__ == "__main__":
    # Epic MELDI Banner
    print(Fore.CYAN + Style.BRIGHT + """
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║       ███╗   ███╗███████╗██╗     ██████╗ ██╗              ║
    ║       ████╗ ████║██╔════╝██║     ██╔══██╗██║              ║
    ║       ██╔████╔██║█████╗  ██║     ██╔══██╗██║              ║
    ║       ██║╚██╔╝██║██╔══╝  ██║     ██╔══██╗██║              ║
    ║       ██║ ╚═╝ ██║███████╗███████╗██████╔╝███████╗         ║
    ║       ╚═╝     ╚═╝╚══════╝╚══════╝╚═════╝ ╚══════╝         ║
    ║                                                          ║
    ║                  Malware Early Light Detection           ║
    ║                       Integrity Tool                     ║
    ║                                                          ║
    ║                Created by: shyclone 🌀                   ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """)
    
    print(Fore.GREEN + Style.BRIGHT + "         🛡️  REAL-TIME FILE TAMPERING DETECTION SYSTEM 🛡️\n")
    
    while True:
        print(Fore.YELLOW + Style.BRIGHT + "┌────────────────────────────────────────────────────────┐")
        print(Fore.YELLOW + Style.BRIGHT + "│                     MELDI CONTROL                      │")
        print(Fore.YELLOW + Style.BRIGHT + "└────────────────────────────────────────────────────────┘\n")
        
        print(Fore.CYAN + "   1. " + Fore.WHITE + Style.BRIGHT + "Create New Baseline" + Fore.GREEN + " (Scan & Save Hashes)")
        print(Fore.CYAN + "   2. " + Fore.WHITE + Style.BRIGHT + "Check for Changes" + Fore.RED + "   (Detect Tampering)")
        print(Fore.CYAN + "   3. " + Fore.MAGENTA + Style.BRIGHT + "Exit\n")
        
        print(Fore.CYAN + Style.DIM + "                  ~ Powered by shyclone ~ 🌀\n")
        
        choice = input(Fore.WHITE + Style.BRIGHT + "Enter your choice (1/2/3): " + Fore.CYAN).strip()
        print()
        
        if choice == "1":
            folder = input(Fore.WHITE + "📂 Enter the full folder path to monitor: " + Fore.CYAN).strip()
            folder = folder.strip('"\'')
            if not os.path.isdir(folder):
                print(Fore.RED + Style.BRIGHT + "❌ Error: Folder not found! Check the path and try again.\n")
            else:
                generate_baseline(folder)
                print(Fore.GREEN + Style.BRIGHT + "✅ Baseline created successfully!\n")
        
        elif choice == "2":
            folder = input(Fore.WHITE + "📂 Enter the full folder path to verify: " + Fore.CYAN).strip()
            folder = folder.strip('"\'')
            if not os.path.isdir(folder):
                print(Fore.RED + Style.BRIGHT + "❌ Error: Folder not found! Check the path and try again.\n")
            else:
                verify_integrity(folder)
        
        elif choice == "3":
            print(Fore.MAGENTA + Style.BRIGHT + "\n🛑 MELDI System Shutting Down...")
            print(Fore.CYAN + Style.BRIGHT + "           Secured & Signed by shyclone 🌀\n")
            break
        
        else:
            print(Fore.RED + Style.BRIGHT + "❌ Invalid choice! Please enter 1, 2, or 3.\n")
