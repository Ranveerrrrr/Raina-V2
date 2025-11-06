
import pyautogui
import time
import subprocess
import os
import random

# Ask for source file (original)
source_file = input("Enter the name of the source file (with extension): ").strip()
if not source_file:
    print("Source filename cannot be empty!")
    exit()

# Ask for target file (where to write)
target_file = input("Enter the name of the target file (with extension): ").strip()
if not target_file:
    print("Target filename cannot be empty!")
    exit()

# Ask for pause settings
try:
    num_pauses = int(input("How many random pauses do you want? (e.g. 2): ").strip())
    max_pause_minutes = float(input("Maximum pause duration (in minutes): ").strip())
except ValueError:
    print("Invalid input! Please enter numbers.")
    exit()

# Convert max pause duration to seconds
max_pause_seconds = int(max_pause_minutes * 60)

# Get absolute paths
script_dir = os.path.dirname(os.path.abspath(__file__))
source_path = os.path.join(script_dir, source_file)
target_path = os.path.join(script_dir, target_file)

# Check if source exists
if not os.path.exists(source_path):
    print(f"Source file not found: {source_path}")
    exit()

# Create target file (empty)
with open(target_path, 'w', encoding='utf-8') as f:
    pass

print(f"Source: {source_path}")
print(f"Target created: {target_path}")

# Open the target file in VS Code
subprocess.Popen([r"C:\Program Files\Microsoft VS Code\Code.exe", target_path])
print("Opening target file in VS Code...")

# Wait for VS Code to open
time.sleep(5)

# Read the content of source file with UTF-8 encoding
with open(source_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Function to type text like a human
def type_like_human(text):
    for char in text:
        pyautogui.write(char)
        time.sleep(0.09)  # Typing speed
    pyautogui.press('enter')

print("Typing started... Press Ctrl+C to stop.")

# Random pause points (choose some random line numbers to pause at)
pause_lines = random.sample(range(len(lines)), min(num_pauses, len(lines)))
pause_lines.sort()

# Main typing loop
try:
    for idx, line in enumerate(lines):
        type_like_human(line.rstrip("\n"))
        time.sleep(0.3)  # Pause between lines

        # If this line is in the chosen pause points, take a break
        if idx in pause_lines:
            pause_duration = random.randint(30, max_pause_seconds)  # At least 30 sec pause
            print(f"\n💤 Taking a thinking break for {pause_duration // 60} min {pause_duration % 60} sec...\n")
            time.sleep(pause_duration)

except KeyboardInterrupt:
    print("\nStopped by user.")
'''
import pyautogui
import time
import subprocess
import os
import random

# Ask for source file (original)
source_file = input("Enter the name of the source file (with extension): ").strip()
if not source_file:
    print("Source filename cannot be empty!")
    exit()

# Ask for target file (where to write)
target_file = input("Enter the name of the target file (with extension): ").strip()
if not target_file:
    print("Target filename cannot be empty!")
    exit()

# Ask for pause settings
try:
    num_pauses = int(input("How many random pauses do you want? (e.g. 2): ").strip())
    max_pause_minutes = float(input("Maximum pause duration (in minutes): ").strip())
except ValueError:
    print("Invalid input! Please enter numbers.")
    exit()

# Convert max pause duration to seconds
max_pause_seconds = int(max_pause_minutes * 60)

# Get absolute paths
script_dir = os.path.dirname(os.path.abspath(__file__))
source_path = os.path.join(script_dir, source_file)
target_path = os.path.join(script_dir, target_file)

# Check if source exists
if not os.path.exists(source_path):
    print(f"Source file not found: {source_path}")
    exit()

# Create target file (empty)
with open(target_path, 'w', encoding='utf-8') as f:
    pass

print(f"Source: {source_path}")
print(f"Target created: {target_path}")

# Open the target file in VS Code
subprocess.Popen([r"C:\Program Files\Microsoft VS Code\Code.exe", target_path])
print("Opening target file in VS Code...")

# Wait for VS Code to open
time.sleep(5)

# Read the content of source file with UTF-8 encoding
with open(source_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Function to type text like a human (no newlines added)
def type_like_human(text):
    for char in text:
        pyautogui.write(char)
        time.sleep(0.09)  # Typing speed

print("Typing started... Press Ctrl+C to stop.")

# Random pause points (choose some random line numbers to pause at)
pause_lines = random.sample(range(len(lines)), min(num_pauses, len(lines)))
pause_lines.sort()

# Main typing loop
try:
    for idx, line in enumerate(lines):
        type_like_human(line.rstrip("\n"))  # type without new line
        time.sleep(0.3)  # Pause between lines (optional)

        # If this line is in the chosen pause points, take a break
        if idx in pause_lines:
            pause_duration = random.randint(30, max_pause_seconds)  # At least 30 sec pause
            print(f"\n💤 Taking a thinking break for {pause_duration // 60} min {pause_duration % 60} sec...\n")
            time.sleep(pause_duration)

except KeyboardInterrupt:
    print("\nStopped by user.")
'''


