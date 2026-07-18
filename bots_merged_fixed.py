import subprocess
import sys
import time

bots = [
    "nzar_updated.py",
    "Hharii (7).py",
    "crips (2).py",
    "fenc (2).py",
    "saddi (1).py",
]

processes = []

for bot in bots:
    try:
        p = subprocess.Popen([sys.executable, bot])
        processes.append(p)
        print(f"Started: {bot}")
    except Exception as e:
        print(f"Failed to start {bot}: {e}")

try:
    while True:
        time.sleep(60)
except KeyboardInterrupt:
    for p in processes:
        p.terminate()
