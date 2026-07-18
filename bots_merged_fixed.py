import subprocess
import time

bots = [
    "/home/bnlafi/Red Dead Bots/nzar_updated.py",
    "/home/bnlafi/Red Dead Bots/animals bot keep files together/Hharii .py",
    "/home/bnlafi/Red Dead Bots/crips.py",
    "/home/bnlafi/Red Dead Bots/fenc.py",
    "/home/bnlafi/Red Dead Bots/saddi.py"
]

for bot in bots:
    subprocess.Popen(["python3.13", bot])

while True:
    time.sleep(60)
