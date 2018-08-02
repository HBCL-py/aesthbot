import sys
import runpy
def glitch(i):
    sys.argv = ["",i]
    return runpy.run_module("jpglitch")
