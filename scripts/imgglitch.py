import sys
import subprocess
import random
ang = str(random.randint(0,360))
blo = str(random.randint(2,15))
inp = str(random.randint(0,2))
def glitch(i):
    return subprocess.check_output(['python', '-m', 'primsort.py', i, "-a", ang, '-b', blo, "-i", "-2", "-I", inp])
