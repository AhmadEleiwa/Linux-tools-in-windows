import os, sys
try:
    os.remove(sys.argv[1])
except:
    os.rmdir(sys.argv[1])