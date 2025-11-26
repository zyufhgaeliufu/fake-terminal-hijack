import os
import random
import time
import sys

def slow_print(text, delay=0.02):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()

def glitch_text(text):
    glitch_chars = "█▓▒░#%@&*!?$<>/\\"
    result = ""
    for c in text:
        if random.random() < 0.06:
            result += random.choice(glitch_chars)
        else:
            result += c
    return result

def clear():
    os.system("cls" if os.name == "nt" else "clear")

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def loading_bar(text):
    print(text)
    bar = ""
    for i in range(20):
        bar += "█"
        print(f"[{bar:<20}] {int((i+1)/20*100)}%", end="\r")
        time.sleep(random.uniform(0.05, 0.15))
    print()

def data_stream(lines=25):
    for _ in range(lines):
        gib = "".join(random.choice("ABCDEF0123456789") for _ in range(48))
        print(CYAN + gib + RESET)
        time.sleep(0.03)

clear()
slow_print("INITIALIZING SYSTEM...", 0.03)
time.sleep(0.7)
clear()

slow_print(CYAN + "ACCESSING SYS32 DIRECTORY..." + RESET)
loading_bar("LOADING KERNEL MODULES...")
time.sleep(0.5)

slow_print(RED + "WARNING: UNAUTHORIZED ACCESS DETECTED" + RESET)
time.sleep(0.6)

loading_bar("OVERRIDING FIREWALL...")
time.sleep(0.4)

slow_print("DOWNLOADING PAYLOAD...")
time.sleep(0.5)
slow_print(RED + "DOWNLOAD FAILED... RETRYING..." + RESET)
time.sleep(0.5)

files = [
    "shadow.dll", "coremap.bin", "system_lock.key",
    "memory_alpha.bin", "ghost_trace.dll",
    "net_override.sys", "root_adm.dat"
]

slow_print("\nSCANNING FILES...")
for f in files:
    slow_print(f"scanning: {f}")
    time.sleep(0.15)

slow_print("\nTRACE ROUTE INITIALIZED...")
ip = f"72.{random.randint(10,99)}.{random.randint(100,199)}.***"
slow_print(f"Tracing route to {ip}")
time.sleep(0.3)
slow_print("Connection routed through 3 proxies")
slow_print("Decrypting route logs...")
loading_bar("PROCESSING TRACE DATA...")

for _ in range(3):
    print(RED + "⚠ SECURITY BREACH ⚠" + RESET)
    time.sleep(0.2)
    clear()

slow_print("STREAMING LIVE SYSTEM LOGS...\n")
data_stream(40)

slow_print(RED + glitch_text("SYSTEM INTEGRITY COMPROMISED...") + RESET)
time.sleep(0.8)
slow_print(YELLOW + glitch_text("FORCING REMOTE OVERRIDE...") + RESET)
time.sleep(0.8)
slow_print(RED + glitch_text("TAKING CONTROL OF TERMINAL...") + RESET)
time.sleep(1)

for i in range(3):
    slow_print(glitch_text("..."), 0.4)

clear()

slow_print(GREEN + "SIMULATION COMPLETE\n" + RESET, 0.02)
slow_print("No changes were made to your system.")
slow_print("This was only a visual simulation.")
slow_print("\nProgram will close in 5 seconds...")

time.sleep(5)
clear()
