import sys
import runpy
def glitch(i):
    sys.argv = ["",i]
    f = runpy.run_module(jpglitch)
    return f
